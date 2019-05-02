class Members:
    def __init__(self, client):
        self.client = client
        self.base = '/members'

    def get(self):
        return self.client.get(self.base)
