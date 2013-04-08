import os
import ConfigParser

import envoy

from mailer import Mailer
from mailer import Message

CONFIG_FILENAME = 'config.ini'
SETTINGS = 'settings'
MAILER = 'mailer'
HOST = 'host'
PORT = 'port'
USERNAME = 'username'
PASSWORD = 'password'
DISPATCH_PATH = 'dispatch_path'
SCRIPT = 'script'
FROM = 'from'
SUBJECT = 'subject'
MAILS = 'mails'

# Engine Supported
engines_supported = ['github', 'bitbucket']


class Config(object):

    def __init__(self, config_file):
        self.config = ConfigParser.ConfigParser()
        self.config_file = config_file
        self.read()

    def _check_config_file(self):
        if not os.path.isfile(self.config_file):
            return False

        return True

    def read(self):
        if self._check_config_file():
            self.config.read(self.config_file)

    def get(self, section, key):
        try:
            return self.config.get(section, key)
        except:
            return None


class Dispatch(object):

    def __init__(self, dp_engine=None, payload=None, config_file=None):
        self.engine = self._load_engine(dp_engine)
        self.dispatch = self.engine.Dispatch(payload)
        self.config = Config(config_file)
        self.config_repo = Config(self.config_file_repo)

    def _load_engine(self, dp_engine):
        if self._check_module(dp_engine):
            engine = __import__('libs.engines.%s' % dp_engine,
                                fromlist=['None'])
        else:
            engine = __import__('libs.engines.ojigi',
                                fromlist=['None'])  # fall backs to ojigi

        return engine

    def _check_module(self, module):
        if module not in engines_supported:
            return False

        return True

    @property
    def dispatch_path(self):
        return self.config.get(SETTINGS, DISPATCH_PATH)

    @property
    def branch(self):
        return self.dispatch.branch

    @property
    def repository(self):
        return self.dispatch.repository

    @property
    def config_file_repo(self):

        return '{0}{1}/{2}'.format(self.dispatch_path,
                                   self.repository, CONFIG_FILENAME)

    @property
    def script_name(self):
        return self.config_repo.get(self.branch, SCRIPT)

    @property
    def mails(self):
        mails = self.config_repo.get(self.branch, MAILS)
        if mails is None:
            return []
        return mails.split('\n')

    def send_mails(self, message=None):

        sender = Mailer(host=self.config.get(MAILER, HOST),
                        port=int(self.config.get(MAILER, PORT)),
                        usr=self.config.get(MAILER, USERNAME),
                        pwd=self.config.get(MAILER, PASSWORD))
        subject = self.config_repo.get(self.branch, SUBJECT)
        subject = subject.format(repository=self.repository, branch=self.branch)

        for mail in self.mails:
            msg = Message(From=self.config_repo.get(self.branch, FROM),
                          To=mail,
                          charset='utf-8')
            msg.Subject = subject
            msg.Body = message
            sender.send(msg)

    def run(self):
        script = "{0}{1}/{2}".format(self.dispatch_path,
                                     self.repository,
                                     self.script_name)
        if os.path.isfile(script):
            r = envoy.run(script)
            return {'status_code': r.status_code,
                    'message': r.std_out,
                    'error': r.std_err}
        else:
            return {'status_code': -1,
                    'error': 'File does not exist'}