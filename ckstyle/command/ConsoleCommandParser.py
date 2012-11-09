import sys
import os
import getopt
import string
from ckstyle.doCssCheck import checkFile, checkDir, checkDirRecursively
import CommandFileParser

def usage():
    print '''
[Usage]
    ckstyle -h / ckstyle --help
    ckstyle file.css
    ckstyle dir 
    ckstyle -r dir
    ckstyle -p file.css
    ckstyle -p -r dir
    ckstyle -c config_file_path
    ckstyle -c config_file_path -r -p
    '''

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
        print '[error] --errorLevel option should be number\n'
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
        print '[error] no config file, ckstyle.ini path should be after -c.\n'
        return None
    if os.path.exists(value) and value.endswith('.ini'):
        return value
    else:
        print '[error] %s does not exist, or is not a ".ini" file' % value
    return None

def parseCmdArgs(config, opts, args, parser):
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

    if configFile is not None :
        parser.load(configFile)
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
        print '[option error] %s ' % e.msg
        return

    configFile = getDefaultConfigPath()
    parser = CommandFileParser.CommandFileParser(configFile)
    config = parser.args

    if len(args) == 0 and len(opts) == 0:
        checkDir(os.getcwd(), config = config)
        return

    config = parseCmdArgs(config, opts, args, parser)
    
    filePath = None
    if len(args) == 0:
        filePath = os.getcwd()
    else:
        filePath = args[0]
        if not os.path.exists(filePath):
            print '[error] %s not exist' % filePath
            return

    if filePath.endswith('.css'):
        checkFile(filePath, config = config)
        return

    checkDir(filePath, config = config)
