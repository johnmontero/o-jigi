# -*- coding: utf8 -*-

import json
import cherrypy


class RootController(object):

    @cherrypy.expose
    def index(self):
        return "o-jigi"

    @cherrypy.expose
    def api(self, payload):
        payload = json.loads(payload)
        branch = payload["commits"][0]['branch']
        return branch