#/usr/bin/python
#encoding=utf-8

import sys
import os
from cssparser.CssFileParser import CssParser
from ckstyle.cmdconsole.ConsoleClass import console
from CssCheckerWrapper import CssChecker
import command.args as args

defaultConfig = args.CommandArgs()

def doCompress(fileContent, fileName = '', config = defaultConfig):
    '''封装一下'''
    parser = CssParser(fileContent, fileName)
    parser.doParse(config)

    checker = CssChecker(parser, config)

    checker.loadPlugins(os.path.realpath(os.path.join(__file__, '../plugins')))
    message = checker.doCompress()

    return checker, message
