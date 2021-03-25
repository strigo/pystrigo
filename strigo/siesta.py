import os
import json

import click  # pytype: disable=pyi-error

from . import utils
from .logger import log
from .client import Strigo


ORG_ID = os.getenv('STRIGO_ORG_ID')
API_KEY = os.getenv('STRIGO_API_KEY')
STRIGO_API_ENDPOINT = os.getenv('STRIGO_API_ENDPOINT', 'https://app.strigo.io/api/v1')

CLICK_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'], token_normalize_func=lambda param: param.lower())


@click.command(context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('METHOD')
@click.argument('ENDPOINT')
@click.argument('ARGUMENTS', nargs=-1)
@click.option('-v', '--verbose', is_flag=True, default=False, help='Set debug level logging')
def _siesta(method, endpoint, arguments, verbose):
    """Easily query Strigo's REST API.

    You can use any method and any endpoint. A few examples:

    * siesta GET classes
    * siesta GET classes :class_id=CLASS_ID
    * siesta POST enrollments :course_id=COURSE_ID email=w00t@200t.com
    * siesta PATCH events :event_id=EVENT_ID name="New Event Name" owner=booboo@doodoo.io
    """
    if verbose:
        log.set_level('DEBUG')

    strigo = Strigo(org_id=ORG_ID, api_key=API_KEY, endpoint=STRIGO_API_ENDPOINT)

    method = method.lower()
    params = {}
    body = {}

    for arg in arguments:
        if arg.startswith(':'):
            key_value = utils.split_kv(arg[1:])
            params[key_value[0]] = key_value[1]
        elif '=' in arg:
            key_value = utils.split_kv(arg)
            try:
                # Try loading JSON first
                body[key_value[0]] = json.loads(key_value[1])
            except (KeyError, json.decoder.JSONDecodeError):
                # And fallback to a string.
                body[key_value[0]] = key_value[1]
    request_endpoint = getattr(getattr(strigo, endpoint), method)

    try:
        if method in ['post', 'patch']:
            request_endpoint(body=body, **params)
        else:
            request_endpoint(**params)
    except TypeError as ex:
        log.error(str(ex))
