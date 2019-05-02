from .. import utils


class Enrollments:
    def __init__(self, client):
        self.client = client
        self.base = '/ondemand/{}/enrollments'

    def get(self, course_id, enrollment_id=None):
        path = utils.join_url(self.base, course_id)
        if enrollment_id:
            path = utils.join_url(self.base, course_id, enrollment_id)

        return self.client.get(path)

    def post(self, course_id, body):
        path = utils.join_url(self.base, course_id)

        return self.client.post(path, body=body)

    def delete(self, course_id, enrollment_id):
        path = utils.join_url(self.base, course_id, enrollment_id)

        return self.client.delete(path)
