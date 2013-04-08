import os
import sys

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = CURRENT_DIR + "".join('/conf/config.ini')
LIBS_DIR = CURRENT_DIR + "".join('/../libs')

if LIBS_DIR not in sys.path:
    sys.path[0:0] = [LIBS_DIR]


from utils import Config


class TestConfig:

    def setup_method(self, method):
        self.config = Config(CONFIG_FILE)

    def test_dispatch_path(self):
        assert self.config.get('settings', 'dispatch_path') == './'

    def test_default_mails(self):
        default_mails = 'user@mail.com\nadmin@mail.com'
        assert self.config.get('settings', 'default_mails') == default_mails

    def test_mailer(self):
        assert self.config.get('mailer', 'host') == 'mailer.smtp'
        assert self.config.get('mailer', 'port') == '20'
        assert self.config.get('mailer', 'username') == 'usermail'
        assert self.config.get('mailer', 'password') == 'password'
