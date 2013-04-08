import os
import sys

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = CURRENT_DIR + "".join('/foo/config.ini')
LIBS_DIR = CURRENT_DIR + "".join('/../libs')

if LIBS_DIR not in sys.path:
    sys.path[0:0] = [LIBS_DIR]


from utils import Config


class TestConfig:

    def setup_method(self, method):
        self.config = Config(CONFIG_FILE)

    def test_script(self):
        assert self.config.get('testing', 'script') == 'testing.sh'

    def test_mails(self):
        mails = 'user@mail.com\nadmin@mail.com'
        assert self.config.get('testing', 'mails') == mails
