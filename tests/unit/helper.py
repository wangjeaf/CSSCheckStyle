import sys
import os

from ckstyle.CssCheckerWrapper import doCheck
from ckstyle.reporter.ReporterUtil import ReporterUtil

def doCssCheck(fileContent, level = 2):
    checker = doCheck(fileContent)
    return checker.errors()

def doCssTextCheck(text, fileName = ''):
    checker = doCheck(text, fileName)
    return checker.errors()
