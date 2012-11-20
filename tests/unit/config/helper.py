import os
import sys
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from asserts import *
import ckstyle.command.CommandFileParser as CommandFileParser
from ckstyle.command.ConsoleCommandParser import parseCmdArgs

def realpath(filepath):
    dirpath = os.path.realpath(os.path.join(__file__, '../'))
    path = os.path.join(dirpath, filepath)
    return path

def parseConfigFile(path):
    parser = CommandFileParser.CommandFileParser(realpath(path), True)
    config = parser.args
    return config
