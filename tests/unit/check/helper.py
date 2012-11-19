import os
import sys
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from asserts import *
from ckstyle.doCssCheck import doCheck

def doCssCheck(fileContent, level = 2):
    checker = doCheck(fileContent)
    return checker.errors()

def doCssTextCheck(text, fileName = ''):
    checker = doCheck(text, fileName)
    return checker.errors()
