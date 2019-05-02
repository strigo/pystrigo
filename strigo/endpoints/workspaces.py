from .. import utils


class Workspaces:
    def __init__(self, client):
        self.client = client
        self.base = '/events/{}/workspaces'

    def get(self, event_id, workspace_id=None):
        path = utils.join_url(self.base, event_id)
        if workspace_id:
            path = utils.join_url(self.base, event_id, workspace_id)

        return self.client.get(path)
