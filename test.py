import sys
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
    return True


if __name__ == '__main__':
    checkCssFileByOpm('test.css')
