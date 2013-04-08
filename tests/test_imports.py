import os
import sys

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = CURRENT_DIR + "".join('/../')

if BASE_DIR not in sys.path:
    sys.path[0:0] = [BASE_DIR]


class TestImports:

    def test_import_root(self):
        try:
            from controllers import root
            imported = True
        except ImportError:
            imported = False
        assert imported

    def test_import_utils(self):
        try:
            from libs import utils
            imported = True
        except ImportError:
            imported = False
        assert imported