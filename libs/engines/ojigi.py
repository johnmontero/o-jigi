# Dispatch default


class Dispatch(object):

    def __init__(self, paylod={}):
        self.paylod = paylod

    @property
    def branch(self):
        return ''

    @property
    def repository(self):
        return ''
