from .. import utils


class Ondemand:
    def __init__(self, client):
        self.client = client
        self.base = '/ondemand'

    def get(self, course_id=None):
        path = self.base
        if course_id:
            path = utils.join_url(self.base, course_id)

        return self.client.get(path)

    def post(self, body):
        path = self.base

        return self.client.post(path, body=body)

    def delete(self, course_id):
        path = utils.join_url(self.base, course_id)

        return self.client.delete(path)
