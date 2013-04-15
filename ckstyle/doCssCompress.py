#/usr/bin/python
#encoding=utf-8

import sys
import os
from .cssparser.CssFileParser import CssParser
from ckstyle.cmdconsole.ConsoleClass import console
from .CssCheckerWrapper import CssChecker
from .command import args as args

defaultConfig = args.CommandArgs()

def prepare(fileContent, fileName = '', config = defaultConfig):
    config.operation = 'compress'
    parser = CssParser(fileContent, fileName)
    parser.doParse(config)
    checker = CssChecker(parser, config)
    checker.loadPlugins(os.path.realpath(os.path.join(__file__, '../plugins')))

    return checker

def doCompress(fileContent, fileName = '', config = defaultConfig):
    '''封装一下'''
    checker = prepare(fileContent, fileName, config)
    message = checker.doCompress()
    return checker, message

def compressFile(filePath, config = defaultConfig):
    extension = config.compressConfig.extension
    if extension.lower() == 'none':
        extension = None
    if extension is not None and filePath.endswith(extension):
        return
    fileContent = open(filePath).read()
    if not config.printFlag:
        console.show('[compress] compressing %s' % filePath)
    path = filePath
    basic = filePath.split('.css')[0]
    if extension is None:
        # 防止替换
        if config.compressConfig.noBak is False:
            open(path + '.bak', 'w').write(fileContent)
    else:
        path = os.path.realpath(filePath.split('.css')[0] + extension)
        
    if config.compressConfig.browsers is None:
        checker, message = doCompress(fileContent, filePath, config)
        if config.printFlag:
            if extension is not None and os.path.exists(path):
                os.remove(path)
            console.show(message)
        else:
            open(path, 'w').write(message)
            console.show('[compress] compressed ==> %s' % path)
    else:
        items = config.compressConfig.browsers.items()
        onlyOne = len(items) == 1
        for key, value in items:
            # 每次都需要一个新的，避免上一次操作后的对象在内存中重复使用导致错误
            # 尤其是合并过的CSS规则集
            checker = prepare(fileContent, filePath, config)
            message = checker.doCompress(value)
            path = os.path.realpath(filePath.split('.css')[0] + '.' + key + '.min.css')
            if config.printFlag:
                if extension is not None and os.path.exists(path):
                    os.remove(path)
                console.show(((key + ' : ') if not onlyOne else '') + message)
            else:
                open(path, 'w').write(message)
                console.show('[compress] compressed ==> %s' % path)

def compressDir(directory, config = defaultConfig):
    if config.recursive:
        compressDirRecursively(directory, config)
    else:
        compressDirSubFiles(directory, config)

def compressDirSubFiles(directory, config = defaultConfig):
    for filename in os.listdir(directory):
        if not filename.endswith('.css') or filename.startswith('_'):
            continue
        compressFile(os.path.join(directory, filename), config)

def compressDirRecursively(directory, config = defaultConfig):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if not filename.endswith('.css') or filename.startswith('_'):
                continue
            compressFile(os.path.join(dirpath, filename), config)
