from helper import *

def doTest():
    fixer, msg = doFix('.test {width:"100px";color:#DDDDDD;}', '')

    styleSheet = fixer.getStyleSheet()
    equal(len(styleSheet.getRuleSets()), 1, 'one ruleset')
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.selector, '.test', 'it is the selector that i need')
    width = ruleSet.getRuleByName('width')
    equal(width.fixedValue,  "'100px'", 'width is fixed')
    equal(width.value, '"100px"', 'value of width is origin')

    color = ruleSet.getRuleByName('color')
    equal(color.fixedValue, '#DDD', 'color is fixed')
    equal(color.value, '#DDDDDD', 'value of color is origin')
