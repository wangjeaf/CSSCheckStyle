import os
import ckstyle.command.CommandFileParser as CommandFileParser
from ckstyle.doCssCheck import doCheck
from ckstyle.reporter.ReporterUtil import ReporterUtil

def doCssCheck(fileContent, level = 2):
    checker = doCheck(fileContent)
    return checker.errors()

def doCssTextCheck(text, fileName = ''):
    checker = doCheck(text, fileName)
    return checker.errors()

def parseConfigFile(path):
    dirpath = os.path.realpath(os.path.join(__file__, '../'))
    path = os.path.join(dirpath, path)
    parser = CommandFileParser.CommandFileParser(path, True)
    config = parser.args
    return config
