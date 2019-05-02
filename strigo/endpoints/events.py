from .. import utils


class Events:
    def __init__(self, client):
        self.client = client
        self.base = '/events'

    def get(self, event_id=None):
        path = self.base
        if event_id:
            path = utils.join_url(self.base, event_id)

        return self.client.get(path)

    def post(self, body):
        path = self.base

        return self.client.post(path, body=body)

    def patch(self, event_id, body):
        path = utils.join_url(self.base, event_id)

        return self.client.patch(path, body=body)

    def delete(self, event_id):
        path = utils.join_url(self.base, event_id)

        return self.client.delete(path)
