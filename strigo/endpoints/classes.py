from .. import utils


class Classes:
    def __init__(self, client):
        self.client = client
        self.base = '/classes'

    def get(self, class_id=None):
        path = self.base
        if class_id:
            path = utils.join_url(self.base, class_id)

        return self.client.get(path)

    def delete(self, class_id):
        path = utils.join_url(self.base, class_id)

        return self.client.delete(path)
