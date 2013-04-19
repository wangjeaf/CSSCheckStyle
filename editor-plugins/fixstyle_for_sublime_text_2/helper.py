
import os
import sys

def getCkstylePath():
    cmdPath = 'ckstyle'
    if sys.platform == 'linux2' or sys.platform == 'darwin':
        returnValue = os.popen3('which ckstyle')
        returnValue = returnValue[1].read() + returnValue[2].read()
        cmdPath = returnValue
    return cmdPath