

class Dispatch(object):

    def __init__(self, paylod=None):
        self.paylod = paylod

    @property
    def branch(self):
        if 'ref' in self.paylod:
            return self.paylod['ref'].replace('refs/heads/', '')
        return ''

    @property
    def name(self):
        if 'repository' in self.paylod:
            if 'name' in self.paylod['repository']:
                return self.paylod['repository']['name']
        return ''
