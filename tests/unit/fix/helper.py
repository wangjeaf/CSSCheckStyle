import os
import sys
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from asserts import *
from ckstyle.doCssFix import doFix
import ckstyle.command.args as args
defaultConfig = args.CommandArgs()

def getFixed(css, name):
    fixer, msg = doFix(css, '')

    ruleSet = fixer.getStyleSheet().getRuleSets()[0]
    rule = ruleSet.getRuleByName(name)
    return rule.fixedValue
