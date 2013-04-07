#/usr/bin/python
#encoding=utf-8

import sys
import os
from reporter.ReporterUtil import ReporterUtil
from cssparser.CssFileParser import CssParser
from ckstyle.cmdconsole.ConsoleClass import console
from CssCheckerWrapper import CssChecker
import command.args as args

defaultConfig = args.CommandArgs()

def doCheck(fileContent, fileName = '', config = defaultConfig):
    '''封装一下'''

    config.operation = 'ckstyle'
    parser = CssParser(fileContent, fileName)
    parser.doParse(config)

    checker = CssChecker(parser, config)

    checker.loadPlugins(os.path.realpath(os.path.join(__file__, '../plugins')))
    checker.doCheck()

    return checker

def checkFile(filePath, config = defaultConfig):
    '''通过路径检查css文件'''
    fileContent = open(filePath).read()
    console.log('[ckstyle] checking %s' % filePath)
    checker = doCheck(fileContent, filePath, config)
    path = os.path.realpath(filePath + config.extension)
    if checker.hasError():
        reporter = ReporterUtil.getReporter('json' if config.exportJson else 'text', checker)
        reporter.doReport()
        if config.printFlag:
            if os.path.exists(path):
                os.remove(path)
            console.show(reporter.export() + '\n')
        else:
            open(path, 'w').write(reporter.export())
            console.show('[ckstyle] @see %s\n' % path)
        return False
    else:
        if config.exportJson:
            console.show('{"status":"ok","result":"%s is ok"}' % filePath)
        else:
            console.show('[ckstyle] %s is ok\n' % filePath)
        if os.path.exists(path):
            os.remove(path)
        return True

def checkDir(directory, config = defaultConfig):
    if config.recursive:
        checkDirRecursively(directory, config)
    else:
        checkDirSubFiles(directory, config)

def checkDirSubFiles(directory, config = defaultConfig):
    for filename in os.listdir(directory):
        if not filename.endswith('.css') or filename.startswith('_'):
            continue
        checkFile(os.path.join(directory, filename), config)

def checkDirRecursively(directory, config = defaultConfig):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if not filename.endswith('.css') or filename.startswith('_'):
                continue
            checkFile(os.path.join(dirpath, filename), config)

def checkCssText(text):
    checker = doCheck(text)
    reporter = ReporterUtil.getReporter('text', checker)
    reporter.doReport()
    console.show(reporter.export())

def main(arg = None):
    if len(sys.argv) == 1:
        console.error('at least two args')
    else:
        if checkCssFileByOpm(sys.argv[1]):
            console.show('no error in %s' % sys.argv[1])

if __name__ == '__main__':
    checkCssFileByOpm(sys.argv[1])
