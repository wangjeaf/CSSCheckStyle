import os
import sys
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from asserts import *
import ckstyle.command.CommandFileParser as CommandFileParser

def parseConfigFile(path):
    dirpath = os.path.realpath(os.path.join(__file__, '../'))
    path = os.path.join(dirpath, path)
    parser = CommandFileParser.CommandFileParser(path, True)
    config = parser.args
    return config
