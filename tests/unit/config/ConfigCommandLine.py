from helper import *

def doTest():
    _default()

def _default():
    config = parseCmdArgs(realpath('ckstyle.ini'), [], [], True)
    equal(config.errorLevel, 0, 'errorLevel is 0')
    equal(config.recursive, False, 'recursive is False')
    equal(config.printFlag, False, 'print flag is False')
    equal(config.include, 'all', 'include is all')
    equal(config.exclude, 'none', 'exclude is none')

    config = parseCmdArgs(realpath('ckstyle.ini'), [("--errorLevel", "2"), ("--include", "abcde"), ("--exclude", "fghi"), ("-p", True), ("-r", True)], [], True)

    equal(config.errorLevel, 2, 'errorLevel is 2')
    equal(config.recursive, True, 'recursive is True')
    equal(config.printFlag, True, 'print flag is True')
    equal(config.include, 'abcde', 'include is abcde')
    equal(config.exclude, 'fghi', 'exclude is fghi')
