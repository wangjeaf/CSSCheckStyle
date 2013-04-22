import os
import sys
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from asserts import *
from ckstyle.command.ConsoleCommandParser import handleFixStyleCmdArgs, handleCkStyleCmdArgs, handleCompressCmdArgs

def doCheck(args):
    return doCkstyle(args, handleCkStyleCmdArgs)
def doFix(args):
    return doCkstyle(args, handleFixStyleCmdArgs)
def doCompress(args):
    return doCkstyle(args, handleCompressCmdArgs)

def doCkstyle(args, handler):
    old = sys.stdout
    output = realpath('_tmp.txt')
    sys.stdout = open(output, 'w')
    handler(args)
    sys.stdout = old

    result = open(output, 'r').read()
    os.remove(output)
    return result.strip()

def realpath(filepath):
    dirpath = os.path.realpath(os.path.join(__file__, '../'))
    path = os.path.join(dirpath, filepath)
    return path