import os
import sys
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from asserts import *
from ckstyle.doCssCompress import doCompress
from ckstyle.browsers.BinaryRule import *

def doCssCompress(fileContent, fileName = ''):
    checker, compressed = doCompress(fileContent, fileName)
    return compressed

def doCssCompress2(fileContent, fileName = ''):
    checker, compressed = doCompress(fileContent, fileName)
    return checker

def realpath(filepath):
    dirpath = os.path.realpath(os.path.join(__file__, '../'))
    path = os.path.join(dirpath, filepath)
    return path

def doCssFileCompress(path):
    fileContent = open(realpath(path), 'r').read()
    return doCssCompress(fileContent, path)

def doCssFileCompress2(path):
    fileContent = open(realpath(path), 'r').read()
    return doCssCompress2(fileContent, path)