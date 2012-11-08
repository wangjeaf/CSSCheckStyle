#/usr/bin/python
#encoding=utf-8

import sys
import os
from reporter.ReporterUtil import ReporterUtil
from cssparser.CssFileParser import CssParser
from CssCheckerWrapper import CssChecker
from entity.StyleSheet import StyleSheet
from command.CommandParser import CommandLineParser, CommandFileParser

def doCheck(fileContent, fileName = ''):
    '''封装一下'''
    parser = CssParser(fileContent)
    css = StyleSheet(fileName)
    parser.doParse(css)

    checker = CssChecker(parser)

    checker.loadPlugins(os.path.realpath(os.path.join(__file__, '../plugins')))
    checker.doCheck()

    return checker

def checkFile(filePath, printFlag = False):
    '''通过路径检查css文件'''
    fileContent = open(filePath).read()
    print '[ckstyle] checking %s' % filePath
    checker = doCheck(fileContent, filePath)
    path = os.path.realpath(filePath + '.ckstyle.txt')
    if checker.hasError():
        reporter = ReporterUtil.getReporter('text', checker)
        reporter.doReport()
        if printFlag:
            print reporter.export(), '\n'
        else:
            open(path, 'w').write(reporter.export())
            print '[ckstyle] @see %s\n' % path
        return False
    else:
        print '[ckstyle] %s is ok\n' % filePath
        if os.path.exists(path):
            os.remove(path)
        return True

def checkDir(directory, printFlag = False):
    for filename in os.listdir(directory):
        if not filename.endswith('.css') or filename.startswith('_'):
            continue
        checkFile(os.path.join(directory, filename), printFlag)

def checkDirRecursively(directory, printFlag = False):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if not filename.endswith('.css') or filename.startswith('_'):
                continue
            checkFile(os.path.join(dirpath, filename), printFlag)

def checkCssText(text):
    checker = doCheck(text)
    reporter = ReporterUtil.getReporter('text', checker)
    reporter.doReport()
    print reporter.export()

def main(arg = None):
    if len(sys.argv) == 1:
        print 'at least two args'
    else:
        if checkCssFileByOpm(sys.argv[1]):
            print 'no error in %s' % sys.argv[1]

if __name__ == '__main__':
    checkCssFileByOpm(sys.argv[1])
