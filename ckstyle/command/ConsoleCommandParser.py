#/usr/bin/python
#encoding=utf-8

import sys
import os
import getopt
import string
from ckstyle.doCssCheck import checkFile, checkDir
from ckstyle.doCssFix import fixFile, fixDir
from ckstyle.doCssCompress import compressFile, compressDir
from ckstyle.cmdconsole.ConsoleClass import console
from ckstyle.command.usage import fixUsage, ckstyleUsage, compressUsage
import CommandFileParser

def usage_compress():
    console.show(compressUsage)

def usage_fix():
    console.show(fixUsage)

def usage_ckstyle():
    console.show(ckstyleUsage)

def getDefaultConfigPath():
    homedir = os.getenv('USERPROFILE') or os.getenv('HOME')
    return os.path.realpath(os.path.join(homedir, 'ckstyle.ini'))

def getConfigFilePath():
    configFile = 'ckstyle.ini'

    if not os.path.exists(configFile):
        configFile = getDefaultConfigPath()

    return configFile

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
    if value == 'none':
        return value
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

def parseCkStyleCmdArgs(defaultConfigFile, opts, args, debug = False, called = False):
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
            if not called:
                usage_ckstyle()
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

    parser = CommandFileParser.CommandFileParser(configFile, debug)
    config = parser.args

    if recur: config.recursive = True
    if printFlag: config.printFlag = True
    if errorLevel: config.errorLevel = errorLevel
    if extension: config.extension = extension
    if include: config.include = include
    if exclude: config.exclude = exclude

    return config

def parseFixStyleCmdArgs(defaultConfigFile, opts, args, debug = False):
    extension = None
    singleLine = None
    safeMode = None
    noBak = None
    for op, value in opts:
        if op == "--help" or op == '-h':
            usage_fix()
            sys.exit()
        elif op == '--fixedExtension':
            extension = getExtension(value)
        elif op == '--singleLine':
            singleLine = True
        elif op == '--safeMode':
            safeMode = True
        elif op == '--noBak':
            noBak = True

    config = parseCkStyleCmdArgs(defaultConfigFile, opts, args, debug, True)

    if extension is not None: config.fixedExtension = extension
    if singleLine is not None: config.fixToSingleLine = singleLine
    if safeMode is not None: config.safeMode = safeMode
    if noBak is not None: config.noBak = noBak
    return config

def parseCompressCmdArgs(defaultConfigFile, opts, args, debug = False):
    #["help", "browsers=", "compressExtension=", "combineFile="]

    browsers = None
    extension = None
    combineFile = None
    safeMode = None
    noBak = None
    for op, value in opts:
        if op == "--help" or op == '-h':
            usage_compress()
            sys.exit()
        elif op == '--compressExtension':
            extension = getExtension(value)
        elif op == '--browsers':
            browsers = getValue(value).lower() == 'true'
        elif op == '--combineFile':
            combineFile = getValue(value).lower() == 'true'
        elif op == '--safeMode':
            safeMode = True
        elif op == '--noBak':
            noBak = True

    config = parseCkStyleCmdArgs(defaultConfigFile, opts, args, debug, True)
    args = config.compressConfig

    if safeMode is not None: config.safeMode = safeMode

    if browsers is not None: args.browsers = browsers
    if extension is not None: args.extension = extension
    if combineFile is not None: args.combineFile = combineFile
    if noBak is not None: args.noBak = noBak

    return config

def _handle(options, dirHandler, fileHandler, argsParser, operation):
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hrpc:", options)
    except getopt.GetoptError, e:
        console.error('[option] %s ' % e.msg)
        return

    configFile = getConfigFilePath()

    if len(args) == 0 and len(opts) == 0:
        parser = CommandFileParser.CommandFileParser(configFile)
        config = parser.args

        dirHandler(os.getcwd(), config = config)
        return

    config = argsParser(configFile, opts, args)
    
    filePath = None
    if len(args) == 0:
        filePath = os.getcwd()
    else:
        filePath = args[0]
        if not os.path.exists(filePath):
            console.error('%s not exist' % filePath)
            return

    if filePath.endswith('.css'):
        fileHandler(filePath, config = config)
    elif os.path.isdir(filePath):
        dirHandler(filePath, config = config)
    else:
        console.error('%s aborted! because "%s" is neither css file, nor dir' % (operation, filePath))

def handleCkStyleCmdArgs():
    options = ["help", "config=", "errorLevel=", "extension=", "include=", "exclude="]
    dirHandler = checkDir
    fileHandler = checkFile
    argsParser = parseCkStyleCmdArgs
    operation = 'ckstyle'
    _handle(options, dirHandler, fileHandler, argsParser, operation)

def handleCompressCmdArgs():
    options = ["help", "config=", "errorLevel=", "extension=", "include=", "exclude=", "browsers=", "compressExtension=", "combineFile=", "safeMode", "noBak"]
    dirHandler = compressDir
    fileHandler = compressFile
    argsParser = parseCompressCmdArgs
    operation = 'compress'
    _handle(options, dirHandler, fileHandler, argsParser, operation)

def handleFixStyleCmdArgs():
    options = ["help", "config=", "errorLevel=", "extension=", "include=", "exclude=", "fixedExtension=", "singleLine", "safeMode", "noBak"]
    dirHandler = fixDir
    fileHandler = fixFile
    argsParser = parseFixStyleCmdArgs
    operation = 'fixstyle'
    _handle(options, dirHandler, fileHandler, argsParser, operation)
