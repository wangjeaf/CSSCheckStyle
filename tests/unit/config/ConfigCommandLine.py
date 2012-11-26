from helper import *

def doTest():
    _default()

def _default():
    config = parseCkStyleCmdArgs(realpath('ckstyle.ini'), [], [], True)
    equal(config.errorLevel, 0, 'errorLevel is 0')
    equal(config.recursive, False, 'recursive is False')
    equal(config.printFlag, False, 'print flag is False')
    equal(config.include, 'all', 'include is all')
    equal(config.exclude, 'none', 'exclude is none')

    equal(config.fixConfig.recursive, False, 'recursive is False')
    equal(config.fixConfig.include, 'all', 'include is all')
    equal(config.fixConfig.exclude, 'none', 'exclude is none')
    equal(config.fixConfig.extension, '.fixed.css', 'extension is .fixed.css')
    equal(config.fixConfig.standard, 'standard.css', 'standard is standard.css')

    equal(config.compressConfig.recursive, False, 'recursive is False')
    equal(config.compressConfig.extension, '.min.css', 'extension is .min.css')
    equal(config.compressConfig.reorder, True, 'reorder is True')
    equal(config.compressConfig.combineAttr, True, 'combine attr is True')
    equal(config.compressConfig.combineRuleSet, True, 'combine ruleset is True')
    equal(config.compressConfig.combineFile, False, 'combine file is False')
    equal(config.compressConfig.browsers, False, 'browsers is false')

    config = parseCkStyleCmdArgs(realpath('ckstyle.ini'), [("--errorLevel", "2"), ("--include", "abcde"), ("--exclude", "fghi"), ("-p", True), ("-r", True)], [], True)

    equal(config.errorLevel, 2, 'errorLevel is 2')
    equal(config.recursive, True, 'recursive is True')
    equal(config.printFlag, True, 'print flag is True')
    equal(config.include, 'abcde', 'include is abcde')
    equal(config.exclude, 'fghi', 'exclude is fghi')
