import os

import click  # pytype: disable=pyi-error

from .logger import log
from .client import Strigo

from . import endpoints


ORG_ID = os.getenv('STRIGO_ORG_ID')
API_KEY = os.getenv('STRIGO_API_KEY')
STRIGO_API_ENDPOINT = os.getenv('STRIGO_API_ENDPOINT', 'https://app.strigo.io/api/v1')

CLICK_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'], token_normalize_func=lambda param: param.lower())


@click.group(name='strigo', context_settings=CLICK_CONTEXT_SETTINGS)
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose output')
def _strigo(verbose):
    if verbose:
        log.set_level('DEBUG')


@_strigo.group(name='ondemand')
def ondemand():
    pass


@ondemand.command(name='enroll')
@click.argument('COURSE_ID')
@click.argument('EMAIL', required=False)
@click.option('-f', '--file', required=False, type=click.Path(exists=True))
def enroll(course_id, email, file):
    """Enroll students to an on-demand course

    COURSE_ID may be either the ID of the course itself, or its external ID.

    --file is path to a file containing a list of newline-delimited email addresses to enroll.

    Note that this doesn't enroll in bulks, but rather makes an API call per enrollment.
    """
    strigo = Strigo(org_id=ORG_ID, api_key=API_KEY, endpoint=STRIGO_API_ENDPOINT)

    if email:
        strigo.enrollments.post(course_id=course_id, body={'email': email})

    if file:
        with open(file) as enrollments_file:
            enrollments = (line.rstrip('\r\n') for line in enrollments_file)
            for enrollment in enrollments:
                if enrollment:
                    strigo.enrollments.post(course_id=course_id, body={'email': enrollment})
