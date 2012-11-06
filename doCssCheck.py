#/usr/bin/python
#encoding=utf-8

import sys
from CssCheckerWrapper import doCheck
from reporter.ReporterUtil import ReporterUtil
from cssparser.CssFileParser import CssParser
from entity.StyleSheet import StyleSheet
from command.CommandParser import CommandLineParser, CommandFileParser

def checkCssFileByOpm(filePath):
    '''通过路径检查css文件，用于OPM'''
    fileContent = open(filePath).read()
    checker = doCheck(fileContent, filePath)
    if checker.hasError():
        reporter = ReporterUtil.getReporter('text', checker)
        reporter.doReport()
        print reporter.export()
        return False
    return True

def checkCssFile(filePath, level):
    fileContent = open(filePath).read()
    checker = doCheck(fileContent, filePath)

    reporter = ReporterUtil.getReporter('text', checker)
    reporter.doReport()
    print reporter.export()
    #open('css-check-result.txt', 'w').write(reporter.export())

def checkCssText(text):
    checker = doCheck(text)
    reporter = ReporterUtil.getReporter('text', checker)
    reporter.doReport()
    print reporter.export()

if __name__ == '__main__':
    checkCssFileByOpm(sys.argv[1])
