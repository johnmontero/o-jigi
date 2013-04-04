import os
import envoy
import cherrypy

DISPATCH_PATH = '/var/www/o-jigi/cmds/'

# Engine Supported
engines_supported = ['github', 'bitbucket']


class Dispatch(object):

    def __init__(self, dp_engine=None, paylod=None):
        self.engine = self._load_engine(dp_engine)
        self.dispatch = self.engine.Dispatch(paylod)

    def _load_engine(self, dp_engine):
        if self._check_module(dp_engine):
            engine = __import__('libs.engines.%s' % dp_engine,
                                fromlist=['None'])
        else:
            engine = __import__('libs.engines.ojigi',
                                fromlist=['None']) # fall backs to ojigi

        return engine

    def _check_module(self, module):
        if module not in engines_supported:
            return False

        return True

    @property
    def branch(self):
        return self.dispatch.branch

    @property
    def name(self):
        return self.dispatch.name

    def run(self):
        file_cmd = '%s%s/run_%s.sh' % (DISPATCH_PATH, self.name, self.branch)
        cherrypy.log('DISPATCH Executing: %s' % file_cmd)
        if os.path.isfile(file_cmd):
            r = envoy.run(file_cmd)
            if r.status_code != 0:
                cherrypy.log('DISPATCH Wrong execution: %s' % file_cmd)
                return {'error': {'cmd': file_cmd, 'out': r.std_out, 'msj': r.std_err}}
            cherrypy.log('DISPATCH Successful Execution: %s' % file_cmd)
            return {'Successful Execution': r.std_out}
        else:
            cherrypy.log('DISPATCH File does not exist: %s' % file_cmd)
            return {'error': 'File does not exist: %s' % file_cmd}
