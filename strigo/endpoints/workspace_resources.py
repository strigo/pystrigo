from .. import utils


class WorkspaceResources:
    def __init__(self, client):
        self.client = client
        self.base = '/events/{event_id}/workspaces/{workspace_id}/resources'

    def get(self, event_id, workspace_id):
        path = utils.join_url(self.base, event_id=event_id, workspace_id=workspace_id)
        return self.client.get(path)
