import os
import sys
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from asserts import *
from ckstyle.browsers.BinaryRule import *
from ckstyle.browsers.Hacks import *
