# -*- coding: utf8 -*-

import json
import requests
import cherrypy

from libs.utils import Dispatch


class RootController(object):

    @cherrypy.expose
    def index(self):
        return "o-jigi"

    @cherrypy.expose
    #@cherrypy.tools.json_out()
    def default(self,*args, **kwargs):

        if cherrypy.request.method == "POST":
            path = "".join(args)
            payload = json.loads(kwargs["payload"])

            dispatch = Dispatch(path.lower(), payload)
            result = dispatch.run()

            subject = u'Sincronización de %s' % dispatch.name

            if'error' in result:
                subject = 'Error: %s' % subject
                msj = result['error']
            else:
                msj = result['Successful Execution']

            return requests.post(
                "https://api.mailgun.net/v2/grup.pe/messages",
                auth=("api", "key-940bh9-k65ujwmo3os4yvui-fm7lbse5"),
                data={"from": "mula2demo <mula2demo@grup.pe>",
                      "to": ["jmonteroc@gmail.com"],
                      "subject": subject,
                      "text": "Repositorio: %s\nRama        :%s\n\n%s"\
                              % (dispatch.name, dispatch.branch, msj)})
