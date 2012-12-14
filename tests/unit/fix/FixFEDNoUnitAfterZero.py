from helper import *

def doTest():
    css = '''html {
        -webkit-tap-highlight-color: rgba(0px, 0px, 0px, 0.1);
    }'''

    fixer, msg = doFix(css, '')

    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    color = ruleSet.getRuleByName('tap-highlight-color')
    equal(color.fixedValue, 'rgba(0, 0, 0, .1)', 'tap-highlight-color is fixed')
    equal(color.value, 'rgba(0px, 0px, 0px, 0.1)', 'tap-highlight-color is ok')
