from .. import utils


class Resources:
    def __init__(self, client):
        self.client = client
        self.base = '/classes/{class_id}/resources'

    def get(self, class_id, resource_id=None):
        path = utils.join_url(self.base, class_id=class_id)
        if resource_id:
            path = utils.join_url(self.base, resource_id, class_id=class_id)

        return self.client.get(path)

    def post(self, class_id, body):
        path = utils.join_url(self.base, class_id=class_id)

        return self.client.post(path, body=body)

    def patch(self, class_id, resource_id, body):
        path = utils.join_url(self.base, resource_id, class_id=class_id)

        return self.client.patch(path, body=body)

    def delete(self, class_id, resource_id):
        path = utils.join_url(self.base, resource_id, class_id=class_id)

        return self.client.delete(path)
