import sys
import os
import getopt
from ckstyle.doCssCheck import checkFile, checkDir, checkDirRecursively
import ConsoleCommandParser
import CommandFileParser

def usage():
    print '''
[Usage]
    ckstyle -h / ckstyle --help
    ckstyle file.css
    ckstyle dir 
    ckstyle -r dir
    ckstyle -c config_file dir 
    ckstyle -c config_file file.css
    '''

def handleCmdArgs():
    opts, args = getopt.getopt(sys.argv[1:], "hrp", ["help"])
    if len(args) == 0 and len(opts) == 0:
        checkDir(os.getcwd())
        return

    recur = False
    printFlag = False
    for op, value in opts:
        if op == "-r":
            recur = True
        if op == '-p':
            printFlag = True
        elif op == "--help" or op == '-h':
            usage()
            sys.exit()

    if len(args) == 0 and recur:
        checkDirRecursively(os.getcwd(), printFlag)
        return

    filePath = args[0]
    if not os.path.exists(filePath):
        print '[error] %s not exist' % filePath
        return

    if filePath.endswith('.css'):
        checkFile(filePath, printFlag)
        return

    if not recur:
        checkDir(filePath, printFlag)
    else:
        checkDirRecursively(filePath, printFlag)

def main():
    handleCmdArgs()

if __name__ == '__main__':
    main()
