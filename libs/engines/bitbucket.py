

class Dispatch(object):

    def __init__(self, paylod=None):
        self.paylod = paylod

    @property
    def branch(self):
        if 'commits' in self.paylod:
            if 'branch' in self.payload['commits'][0]:
                return  self.payload['commits'][0]['branch']
        return ''

    @property
    def name(self):
        if 'repository' in self.paylod:
            if 'name' in self.paylod['repository']:
                return self.paylod['repository']['name']
        return ''
