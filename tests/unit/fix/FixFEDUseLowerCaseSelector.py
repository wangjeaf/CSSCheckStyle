from helper import *

def doTest():
    _lower()
    _upper()

def _lower():
    fixer = doFix('.test {width:100px;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.fixedSelector, '.test', 'selector lower is ok')

def _upper():
    fixer = doFix('.TEST {width:100px;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.fixedSelector, '.test', 'selector all upper is ok')

    fixer = doFix('.Test {width:100px;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.fixedSelector, '.test', 'selector one upper is ok')

    fixer = doFix('.Test-WRAPPER {width:100px;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.fixedSelector, '.test-wrapper', 'selector upper with - is ok')
