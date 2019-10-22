from .. import utils


class EventUsage:
    def __init__(self, client):
        self.client = client
        self.base = '/events/{event_id}/usage'

    def get(self, event_id):
        path = utils.join_url(self.base, event_id=event_id)

        return self.client.get(path)
