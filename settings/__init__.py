from __future__ import absolute_import, print_function

import sys

try:
    from .develop import *
    print("Trying import develop.py settings...", file=sys.stderr)
except ImportError:
    print("Trying import settings.py settings...", file=sys.stderr)
    from .settings import *
