#/usr/bin/python
#encoding=utf-8

import sys
import os
import getopt
import string
from ckstyle.doCssCheck import checkFile, checkDir, checkDirRecursively
from ckstyle.cmdconsole.ConsoleClass import console
import CommandFileParser

def usage():
    console.show('''
[Usage]
    ckstyle -h / ckstyle --help
    ckstyle
    ckstyle file.css
    ckstyle dir 
    ckstyle -r dir
    ckstyle -p -r dir
    ckstyle -c xxx.ini 
    ckstyle -c xxx.ini -r -p

[Example]
    ckstyle -c xxx.ini -r -p -c xxx.ini --extension=.test.txt --include=all --exclude=none --errorLevel=2 dirpath

[Options]
    -h / --help     show help
    -r              check files in directory recursively
    -p              print check result to console(delete result files at the same time)
    -c / --config   specify the config file name(use "~/ckstyle.ini" as default)
    --include       specify rules(can be configed in .ini file)
    --exclude       specify exclude rules(can be configed in .ini file)
    --extension     specify check result file extension(use ".ckstyle.txt" as default)
    --errorLevel    specify error level(0-error, 1-warning, 2-log)
    ''')

def getDefaultConfigPath():
    homedir = os.getenv('USERPROFILE') or os.getenv('HOME')
    return os.path.realpath(os.path.join(homedir, 'ckstyle.ini'))

def getErrorLevel(value):
    if value.strip() == '':
        return None
    try:
        realValue = string.atoi(value)
        errorLevel = realValue
        if errorLevel > 2:
            errorLevel = 2
        elif errorLevel < 0:
            errorLevel = 0
        return errorLevel
    except ValueError:
        console.error('--errorLevel option should be number\n')
        return None

def getExtension(value):
    if value.strip() == '':
        return None
    value = value.strip()
    if not value.startswith('.'):
        value = '.' + value
    return value

def getValue(value):
    if value.strip() == '':
        return None
    return value.strip()

def getConfigFile(value):
    value = value.strip()
    if value == '':
        console.error('no config file, ckstyle.ini path should be after -c.\n')
        return None
    if os.path.exists(value) and value.endswith('.ini'):
        return value
    else:
        console.error('%s does not exist, or is not a ".ini" file' % value)
    return None

def parseCmdArgs(defaultConfigFile, opts, args):
    recur = False
    printFlag = False
    configFile = None
    errorLevel = None
    extension = None
    include = None
    exclude = None
    for op, value in opts:
        if op == "-r":
            recur = True
        elif op == '-p':
            printFlag = True
        elif op == '-c' or op == '-config':
            configFile = getConfigFile(value)
        elif op == "--help" or op == '-h':
            usage()
            sys.exit()
        elif op == '--extension':
            extension = getExtension(value)
        elif op == '--errorLevel':
            errorLevel = getErrorLevel(value)
        elif op == '--include':
            include = getValue(value)
        elif op == '--exclude':
            exclude = getValue(value)

    if configFile is None :
        configFile = defaultConfigFile

    parser = CommandFileParser.CommandFileParser(configFile)
    config = parser.args

    if recur: config.recursive = True
    if printFlag: config.printFlag = True
    if errorLevel: config.errorLevel = errorLevel
    if extension: config.extension = extension
    if include: config.include = include
    if exclude: config.exclude = exclude

    return config

def handleCmdArgs():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hrpc:", ["help", "config=", "errorLevel=", "extension=", "include=", "exclude="])
    except getopt.GetoptError, e:
        console.error('[option] %s ' % e.msg)
        return

    configFile = 'ckstyle.ini'

    if not os.path.exists(configFile):
        configFile = getDefaultConfigPath()

    if len(args) == 0 and len(opts) == 0:
        parser = CommandFileParser.CommandFileParser(configFile)
        config = parser.args

        checkDir(os.getcwd(), config = config)
        return

    config = parseCmdArgs(configFile, opts, args)
    
    filePath = None
    if len(args) == 0:
        filePath = os.getcwd()
    else:
        filePath = args[0]
        if not os.path.exists(filePath):
            console.error('%s not exist' % filePath)
            return

    if filePath.endswith('.css'):
        checkFile(filePath, config = config)
    elif os.path.isdir(filePath):
        checkDir(filePath, config = config)
    else:
        console.error('check aborted! because "%s" is neither css file, nor dir' % filePath)
