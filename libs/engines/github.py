

class Dispatch(object):

    def __init__(self, payload=None):
        self.payload = payload

    @property
    def branch(self):
        if 'ref' in self.payload:
            return self.payload['ref'].replace('refs/heads/', '')
        return ''

    @property
    def repository(self):
        if 'repository' in self.payload:
            if 'name' in self.payload['repository']:
                return self.payload['repository']['name']
        return ''
