# -*- coding: utf8 -*-
import os
import sys
sys.stdout = sys.stderr

import cherrypy
from controllers.root import RootController
from werkzeug.debug import DebuggedApplication

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
LIBS_DIR = CURRENT_DIR + "".join('/libs')

if LIBS_DIR not in sys.path:
    sys.path[0:0] = [LIBS_DIR]

server_conf = {
    'global': {
        'error_page.404': CURRENT_DIR + "".join('/templates/404.html')
    },
    }

app_conf = {
    '/static': {
        'tools.staticdir.root': CURRENT_DIR,
        'tools.staticdir.debug': True,
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'static'
    }
}


if __name__ == "__main__":
    cherrypy.config.update(server_conf)
    cherrypy.quickstart(RootController(), '/', app_conf)
else:
    def application(environ, start_response):
        cherrypy.config.update(server_conf)
        cherrypy.tree.mount(RootController(), '/', app_conf)
        return cherrypy.tree(environ, start_response)

    application = DebuggedApplication(application, evalex=True)