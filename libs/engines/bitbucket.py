

class Dispatch(object):

    def __init__(self, payload=None):
        self.payload = payload

    @property
    def branch(self):
        if 'commits' in self.payload:
            if 'branch' in self.payload['commits'][0]:
                return  self.payload['commits'][0]['branch']
        return ''

    @property
    def repository(self):
        if 'repository' in self.payload:
            if 'name' in self.payload['repository']:
                return self.payload['repository']['name']
        return ''
