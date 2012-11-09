import sys
import os
import getopt
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
    '''

def getDefaultConfigPath():
    homedir = os.getenv('USERPROFILE') or os.getenv('HOME')
    return os.path.realpath(os.path.join(homedir, 'ckstyle.ini'))

def handleCmdArgs():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hrpc", ["help"])
    except getopt.GetoptError, e:
        print '[option error] %s ' % e.msg
        return

    configFile = getDefaultConfigPath()
    parser = CommandFileParser.CommandFileParser(configFile)
    config = parser.args

    if len(args) == 0 and len(opts) == 0:
        checkDir(os.getcwd(), config = config)
        return

    recur = False
    printFlag = False
    configFile = None
    for op, value in opts:
        if op == "-r":
            recur = True
        if op == '-p':
            printFlag = True
        if op == '-c':
            if value == '':
                print '[error] no config file, ckstyle.ini path should be after -c.\n'
                continue
            if os.path.exists(value):
                configFile = value
            else:
                print '[error] %s does not exist' % value
        elif op == "--help" or op == '-h':
            usage()
            sys.exit()

    if configFile is not None and configFile.endswith('ckstyle.ini'):
        parser.load(configFile)
        config = parser.args

    if recur:
        config.recursive = True

    if printFlag:
        config.printFlag = True

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
