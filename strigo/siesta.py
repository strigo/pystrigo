import os

import click  # pytype: disable=pyi-error

from . import utils
from .logger import log
from .client import Strigo


@click.command()
@click.argument('METHOD')
@click.argument('ENDPOINT')
@click.argument('ARGUMENTS', nargs=-1)
@click.option('-v', '--verbose', is_flag=True, default=False, help='Set debug level logging')
def request(method, endpoint, arguments, verbose):
    if verbose:
        log.set_level('DEBUG')

    org_id = os.getenv('STRIGO_ORG_ID')
    api_key = os.getenv('STRIGO_API_KEY')
    strigo_api_endpoint = os.getenv('STRIGO_API_ENDPOINT')

    assert org_id
    assert api_key
    assert strigo_api_endpoint
    strigo = Strigo(org_id=org_id, api_key=api_key, endpoint=strigo_api_endpoint)

    method = method.lower()
    params = {}
    body = {}

    for arg in arguments:
        if arg.startswith(':'):
            key_value = utils.split_kv(arg[1:])
            params[key_value[0]] = key_value[1]
        elif '=' in arg:
            key_value = utils.split_kv(arg)
            body[key_value[0]] = key_value[1]

    request_endpoint = getattr(getattr(strigo, endpoint), method)

    try:
        if method in ['post', 'patch']:
            request_endpoint(body=body, **params)
        else:
            request_endpoint(**params)
    except TypeError as ex:
        log.error(str(ex))
