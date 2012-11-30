from helper import *

def doTest():
    _lower()
    _upper()

def _lower():
    fixer, msg = doFix('.test {width:100px;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.fixedSelector, '.test', 'selector lower is ok')

def _upper():
    # if fix upper to lower, will cause error in HTML, do not do evil
    return
    fixer, msg = doFix('.TEST {width:100px;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.fixedSelector, '.test', 'selector all upper is ok')

    fixer, msg = doFix('.Test {width:100px;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.fixedSelector, '.test', 'selector one upper is ok')

    fixer, msg = doFix('.Test-WRAPPER {width:100px;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.fixedSelector, '.test-wrapper', 'selector upper with - is ok')
