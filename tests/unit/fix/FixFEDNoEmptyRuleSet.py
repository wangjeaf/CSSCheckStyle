from helper import *

def doTest():
    fixer, msg = doFix('.test {} .test2 {} .test3 {width:100px;} .test4 {}', '')

    styleSheet = fixer.getStyleSheet()
    equal(len(styleSheet.getRuleSets()), 1, 'one ruleset')
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.selector, '.test3', 'it is test3')
    width = ruleSet.getRuleByName('width')
    equal(width.fixedValue,  "100px", 'width is fixed')
    equal(width.value, '100px', 'value of width is origin')
