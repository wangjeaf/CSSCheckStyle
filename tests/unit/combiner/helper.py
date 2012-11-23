import os
import sys
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from asserts import *
from ckstyle.doCssCompress import doCompress

def doCssCompress(fileContent, fileName = ''):
    checker, compressed = doCompress(fileContent, fileName)
    return compressed

def realpath(filepath):
    dirpath = os.path.realpath(os.path.join(__file__, '../'))
    path = os.path.join(dirpath, filepath)
    return path

def doCssFileCompress(path):
    fileContent = open(realpath(path), 'r').read()
    return doCssCompress(fileContent, path)
