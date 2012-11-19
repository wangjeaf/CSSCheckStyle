from asserts import *
from helper import parseConfigFile

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
    equal(config.tabSpaces, 2, 'tab spaces is 2 from config file')
    equal(config.standard, 'standard3.css', 'standard css file name is ok')
    equal(len(config.ignoreRuleSets), 1, 'two ignored rule sets')

def _configed():
    config = parseConfigFile('ckstyle_configed.ini')
    equal(config.errorLevel, 2, 'error level is 2(LOG)')
    equal(config.printFlag, True, 'print flag is true')
    equal(config.extension, '.ckstyle2.txt', 'extension is ok')
    equal(config.include, 'abc', 'include is abc')
    equal(config.exclude, 'ddd', 'exclude is ddd')
    equal(config.tabSpaces, 2, 'tab spaces is 2')
    equal(config.standard, 'standard2.css', 'standard css file name is ok')
    equal(config.ignoreRuleSets[0], '@unit-test-expecteds', 'rule sets ignored')
    equal(config.ignoreRuleSets[1], '@unit-tests-fda', 'rule sets ignored')
    equal(len(config.ignoreRuleSets), 2, 'two ignored rule sets')

def _default():
    config = parseConfigFile('ckstyle.ini')
    equal(config.errorLevel, 0, 'error level is 0(ERROR)')
    equal(config.printFlag, False, 'print flag is false')
    equal(config.extension, '.ckstyle.txt', 'extension is ok')
    equal(config.include, 'all', 'include is all')
    equal(config.exclude, 'none', 'exclude is none')
    equal(config.tabSpaces, 4, 'tab spaces is 4')
    equal(config.standard, 'standard.css', 'standard css file name is ok')
    equal(config.ignoreRuleSets[0], '@unit-test-expecteds', 'rule sets ignored')
    equal(len(config.ignoreRuleSets), 1, 'only one ignored rule set')
