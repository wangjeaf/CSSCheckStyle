import sys
import os
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from CssCheckerWrapper import doCheck
from reporter.ReporterUtil import ReporterUtil

def doCssCheck(fileContent, level = 2):
    checker = doCheck(fileContent)
    return checker.errors()

def doCssTextCheck(text, fileName = ''):
    checker = doCheck(text, fileName)
    return checker.errors()
