# -*- coding: utf8 -*-
import os
import sys
sys.stdout = sys.stderr

import atexit
import cherrypy
from controllers.root import RootController
from werkzeug.debug import DebuggedApplication

current_dir = os.path.dirname(os.path.abspath(__file__))

server_conf = {
    'global': {
        'error_page.404': 'templates/404.html'
    }
}

app_conf = {
    '/static': {
        'tools.staticdir.debug': True,
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(current_dir, 'static')
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