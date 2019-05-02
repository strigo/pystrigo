from .. import utils


class Partners:
    def __init__(self, client):
        self.client = client
        self.base = '/partners'

    def get(self, partner_id=None):
        path = self.base
        if partner_id:
            path = utils.join_url(self.base, partner_id)

        return self.client.get(path)

    def post(self, body):
        path = self.base

        return self.client.post(path, body=body)

    def patch(self, partner_id, body):
        path = utils.join_url(self.base, partner_id)

        return self.client.patch(path, body=body)

    def delete(self, partner_id):
        path = utils.join_url(self.base, partner_id)

        return self.client.delete(path)


class PartnerMembers:
    def __init__(self, client):
        self.client = client
        self.base = '/partners/{}/members'

    def get(self, partner_id):
        path = utils.join_url(self.base, partner_id)

        return self.client.get(path)

    def post(self, partner_id, body):
        path = utils.join_url(self.base, partner_id)

        return self.client.post(path, body=body)

    def patch(self, partner_id, body):
        path = utils.join_url(self.base, partner_id)

        return self.client.post(path, body=body)
