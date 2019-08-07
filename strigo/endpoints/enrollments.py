from .. import utils


class Enrollments:
    def __init__(self, client):
        self.client = client
        self.base = '/ondemand/{course_id}/enrollments'

    def get(self, course_id, enrollment_id=None):
        path = utils.join_url(self.base, course_id=course_id)
        if enrollment_id:
            path = utils.join_url(self.base, enrollment_id, course_id=course_id)

        return self.client.get(path)

    def post(self, course_id, body):
        path = utils.join_url(self.base, course_id=course_id)

        return self.client.post(path, body=body)

    def patch(self, course_id, enrollment_id, body):
        path = utils.join_url(self.base, enrollment_id, course_id=course_id)

        return self.client.patch(path, body=body)

    def delete(self, course_id, enrollment_id):
        path = utils.join_url(self.base, enrollment_id, course_id=course_id)

        return self.client.delete(path)
