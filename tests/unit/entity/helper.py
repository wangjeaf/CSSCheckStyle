import os
import sys
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from asserts import *


from ckstyle.entity.Rule import Rule
from ckstyle.entity.RuleSet import RuleSet
from ckstyle.entity.StyleSheet import StyleSheet
from ckstyle.entity.ExtraStatement import ExtraStatement
