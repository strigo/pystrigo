import json

# pytype: disable=pyi-error
import requests
from requests.packages import urllib3

from box import Box
# pytype: enable=pyi-error

from . import endpoints
from .logger import log


DEFAULT_STRIGO_API_URL = 'https://app.strigo.io/api/v1'

urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)


class _Response:
    def __init__(self, status_code, payload=None, use_box=False):
        self.status_code = status_code
        self.result = payload.get('result') if payload else None

        data = payload.get('data') if payload else {}
        self.data = Box(data) if use_box else data

        error = payload.get('error') if payload else {}
        self.error = Box(error) if use_box else error


class _HTTPClient:
    def __init__(self, org_id, api_key, endpoint, use_box=False):
        self.endpoint = endpoint
        self.api_key = api_key
        self.headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}:{}'.format(org_id, api_key)
        }
        self.use_box = use_box

    def _request(self, method, path, body=None):
        body = body or {}
        url = self.endpoint + path

        log.info('{} {}...'.format(method.upper(), path), **body)
        response = getattr(requests, method)(url, json=body, headers=self.headers)
        log.info(
            '{} {} response'.format(method.upper(), path),
            status_code=response.status_code,
            # We return 201 on successful `delete` with no data.
            data=json.dumps(json.loads(response.text), indent=4) if response.text else None
        )
        return _Response(
            response.status_code,
            response.json() if method != 'delete' else None,
            use_box=self.use_box)

    def get(self, path, body=None):
        return self._request('get', path, body)

    def post(self, path, body=None):
        return self._request('post', path, body)

    def patch(self, path, body=None):
        return self._request('patch', path, body)

    def delete(self, path, body=None):
        return self._request('delete', path, body)


class Strigo:
    def __init__(self, org_id, api_key, endpoint=DEFAULT_STRIGO_API_URL, use_box=False):
        self._client = _HTTPClient(org_id, api_key, endpoint, use_box)

        self.events = endpoints.Events(self._client)
        self.classes = endpoints.Classes(self._client)
        self.members = endpoints.Members(self._client)
        self.partners = endpoints.Partners(self._client)
        self.ondemand = endpoints.Ondemand(self._client)
        self.resources = endpoints.Resources(self._client)
        self.workspaces = endpoints.Workspaces(self._client)
        self.enrollments = endpoints.Enrollments(self._client)
        self.presentations = endpoints.Presentations(self._client)
        self.partner_members = endpoints.PartnerMembers(self._client)
        self.presentation_notes = endpoints.PresentationNotes(self._client)
        self.workspace_resources = endpoints.WorkspaceResources(self._client)
