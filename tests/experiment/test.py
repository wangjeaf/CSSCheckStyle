import sys
import os

from ckstyle.CssCheckerWrapper import doCheck
from ckstyle.reporter.ReporterUtil import ReporterUtil
from ckstyle.cssparser.CssFileParser import CssParser
from ckstyle.entity.StyleSheet import StyleSheet

def checkCssFileByOpm(filePath):
    fileContent = open(filePath).read()
    checker = doCheck(fileContent, filePath)
    if checker.hasError():
        reporter = ReporterUtil.getReporter('text', checker)
        reporter.doReport()
        print reporter.export()
        return False
    else:
        print 'no error'
        return True

if __name__ == '__main__':
    checkCssFileByOpm('test/test.css')
