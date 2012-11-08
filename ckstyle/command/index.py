import sys
import os
import getopt
from ckstyle.doCssCheck import checkFile, checkDir, checkDirRecursively
import ConsoleCommandParser
import CommandFileParser

def usage():
    print '''
[Usage]
    run ckstyle by : 
    1. ckstyle file.css
    2. ckstyle dir / ckstyle -r dir
    3. ckstyle -c config_file dir / ckstyle -c config_file file.css
    '''

def checkDir(directory):
    for filename in os.listdir(directory):
        if not filename.endswith('.css') or filename.startswith('_'):
            continue
        checkFile(filename)
    
def handleCmdArgs():
    opts, args = getopt.getopt(sys.argv[1:], "hr", ["help"])
    if len(args) == 0 and len(opts) == 0:
        checkDir(os.getcwd())
        return

    recur = False
    for op, value in opts:
        if op == "-r":
            recur = True
        elif op == "--help" or op == '-h':
            usage()
            sys.exit()

    if len(args) == 0 and recur:
        checkDirRecursively(os.getcwd())
        return

    filePath = args[0]
    if not os.path.exists(filePath):
        print '[error] %s not exist' % filePath
        return

    if filePath.endswith('.css'):
        checkFile(filePath)
        return

    if not recur:
        checkDir(filePath)
    else:
        checkDirRecursively(filePath)

def main():
    handleCmdArgs()

if __name__ == '__main__':
    main()
