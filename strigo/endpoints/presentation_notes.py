from .. import utils


class PresentationNotes:
    def __init__(self, client):
        self.client = client
        self.base = '/classes/{class_id}/presentations/{presentation_id}/notes'

    def get(self, class_id, presentation_id):
        path = utils.join_url(self.base, presentation_id=presentation_id, class_id=class_id)

        return self.client.get(path)

    def post(self, class_id, presentation_id, body):
        path = utils.join_url(self.base, presentation_id=presentation_id, class_id=class_id)

        return self.client.post(path, body=body)

    def delete(self, class_id, presentation_id):
        path = utils.join_url(self.base, presentation_id=presentation_id, class_id=class_id)

        return self.client.delete(path)
