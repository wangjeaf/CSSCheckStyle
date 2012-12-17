#/usr/bin/python
#encoding=utf-8

import sys
import os
from cssparser.CssFileParser import CssParser
from ckstyle.cmdconsole.ConsoleClass import console
from CssCheckerWrapper import CssChecker
import command.args as args

defaultConfig = args.CommandArgs()

def doFix(fileContent, fileName = '', config = defaultConfig):
    '''封装一下'''
    parser = CssParser(fileContent, fileName)
    parser.doParse(config)

    checker = CssChecker(parser, config)

    checker.loadPlugins(os.path.realpath(os.path.join(__file__, '../plugins')))
    fixed = checker.doFix()

    return checker, fixed

def fixFile(filePath, config = defaultConfig):
    extension = config.fixedExtension
    if extension.lower() == 'none':
        extension = None
    if extension is not None and filePath.endswith(extension):
        return
    fileContent = open(filePath).read()
    if not config.printFlag:
        console.show('[fixstyle] fixing %s' % filePath)

    checker, msg = doFix(fileContent, filePath, config)

    path = filePath
    if extension is None:
        if config.noBak is False:
            open(path + '.bak', 'w').write(fileContent)
    else:
        path = os.path.realpath(filePath.split('.css')[0] + extension)

    if config.printFlag:
        if extension is not None and os.path.exists(path):
            os.remove(path)
        console.show(msg)
    else:
        open(path, 'w').write(msg)
        console.show('[fixstyle] fixed ==> %s' % path)

def fixDir(directory, config = defaultConfig):
    if config.recursive:
        fixDirRecursively(directory, config)
    else:
        fixDirSubFiles(directory, config)

def fixDirSubFiles(directory, config = defaultConfig):
    for filename in os.listdir(directory):
        if not filename.endswith('.css') or filename.startswith('_'):
            continue
        fixFile(os.path.join(directory, filename), config)

def fixDirRecursively(directory, config = defaultConfig):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if not filename.endswith('.css') or filename.startswith('_'):
                continue
            fixFile(os.path.join(dirpath, filename), config)
