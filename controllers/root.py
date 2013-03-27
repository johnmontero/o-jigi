# -*- coding: utf8 -*-

import json
import cherrypy

from libs.utils import Dispatch


class RootController(object):

    @cherrypy.expose
    def index(self):
        return "o-jigi"

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def default(self,*args, **kwargs):

        if cherrypy.request.method == "POST":
            path = "".join(args)
            payload = json.loads(kwargs["payload"])

            dispatch = Dispatch(path.lower(), payload)
            return dispatch.run()
