import sys
# TODO will change to ckstyle.command.commandLineHandler
from ckstyle.doCssCheck import checkCssFileByOpm

if __name__ == '__main__':
    # TODO will change to commandLineHandler.handle()
    if len(sys.argv) == 1:
        print 'at least two args'
    else:
        if checkCssFileByOpm(sys.argv[1]):
            print 'no error in %s' % sys.argv[1]
