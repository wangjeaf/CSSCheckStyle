import sys
from ckstyle.doCssCheck import doCheck
from ckstyle.doCssFix import doFix
from ckstyle.doCssCompress import doCompress
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
    return True

def fixCss(filePath):
    fileContent = open(filePath).read()
    checker = doFix(fileContent, filePath)
    print checker.parser.styleSheet.getRuleSets()[0].values
    print checker.parser.styleSheet.getRuleSets()[0].getRules()[0].fixedValue

def compressCss(filePath):
    fileContent = open(filePath).read()
    checker, content = doCompress(fileContent, filePath)
    print content

if __name__ == '__main__':
    #fixCss('test.css')
    #checkCssFileByOpm('test.css')
    compressCss('test.css')
