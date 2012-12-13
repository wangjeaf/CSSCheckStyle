from helper import *

def doTest():
    _default()
    _configed()
    _missing()

def _missing():
    config = parseConfigFile('ckstyle_missing.ini')
    equal(config.errorLevel, 2, 'error level is 0(ERROR) from python')
    equal(config.printFlag, False, 'print flag is False from python')
    equal(config.extension, '.ckstyle.txt', 'extension is ok from python')
    equal(config.include, 'all', 'include is all from python')
    equal(config.exclude, 'none', 'exclude is none from python')
    equal(config.standard, 'standard3.css', 'standard css file name is ok')
    equal(config.fixedExtension, '.fixed2.css', 'fixed extension is ok from python')
    equal(config.fixToSingleLine, False, 'fix to single line is false')
    equal(config.safeMode, False, 'safemode is false by file')
    equal(len(config.ignoreRuleSets), 1, 'one ignored rule set')

    args = config.compressConfig
    equal(args.combineFile, True, 'combine file is still True')
    equal(args.browsers, False, 'browsers is false')
    equal(args.extension, '.lala.min.css', 'extension changed')

def _configed():
    config = parseConfigFile('ckstyle_configed.ini')
    equal(config.errorLevel, 2, 'error level is 2(LOG)')
    equal(config.printFlag, True, 'print flag is true')
    equal(config.extension, '.ckstyle2.txt', 'extension is ok')
    equal(config.include, 'abc', 'include is abc')
    equal(config.exclude, 'ddd', 'exclude is ddd')
    equal(config.standard, 'standard2.css', 'standard css file name is ok')
    equal(config.ignoreRuleSets[0], '@unit-test-expecteds', 'rule sets ignored')
    equal(config.ignoreRuleSets[1], '@unit-tests-fda', 'rule sets ignored')
    equal(len(config.ignoreRuleSets), 2, 'two ignored rule sets')
    equal(config.fixToSingleLine, True, 'fix to single line is true')
    equal(config.safeMode, True, 'safemode is True by file')

    args = config.compressConfig
    equal(args.combineFile, True, 'combine file is True')
    equal(args.browsers, True, 'browsers is True')
    equal(args.extension, '.min3.css', 'extension changed')

def _default():
    config = parseConfigFile('ckstyle.ini')
    equal(config.errorLevel, 0, 'error level is 0(ERROR)')
    equal(config.printFlag, False, 'print flag is false')
    equal(config.extension, '.ckstyle.txt', 'extension is ok')
    equal(config.include, 'all', 'include is all')
    equal(config.exclude, 'none', 'exclude is none')
    equal(config.standard, 'standard.css', 'standard css file name is ok')
    equal(config.ignoreRuleSets[0], '@unit-test-expecteds', 'rule sets ignored')
    equal(len(config.ignoreRuleSets), 1, 'only one ignored rule set')
    equal(config.fixToSingleLine, False, 'fix to single line is false default')
    equal(config.safeMode, False, 'safemode is False by file')
