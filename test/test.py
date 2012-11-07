import sys
import sys
import os
sys.path.insert(0, os.path.realpath(os.path.join(__file__, '../../')))
for p in os.environ.get('PYTHONPATH', '').split(';'):
    sys.path.append(p)

from CssCheckerWrapper import doCheck
from reporter.ReporterUtil import ReporterUtil
from cssparser.CssFileParser import CssParser
from entity.StyleSheet import StyleSheet

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
    checkCssFileByOpm('test.css')
