from helper import *

def doTest():
    fixer = doFix('.test {color1:#DDD;color2:#DDDDDD;color3:#dddddd;color4:#ddd;color5:#DDFFCC;color6:#ABCDEF;color7:#ABCDEFGH;color8:#abcdef;color9:#ffff;color10:#f;}', '')

    styleSheet = fixer.getStyleSheet()
    equal(len(styleSheet.getRuleSets()), 1, 'one ruleset')
    equal(len(styleSheet.getRuleSets()[0].getRules()), 10, 'ten rules')

    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.getRuleByName('color1').fixedValue, '#DDD', 'color1 ok')
    equal(ruleSet.getRuleByName('color2').fixedValue, '#DDD', 'color2 ok')
    equal(ruleSet.getRuleByName('color3').fixedValue, '#DDD', 'color3 ok')
    equal(ruleSet.getRuleByName('color4').fixedValue, '#DDD', 'color4 ok')
    equal(ruleSet.getRuleByName('color5').fixedValue, '#DFC', 'color5 ok')
    equal(ruleSet.getRuleByName('color6').fixedValue, '#ABCDEF', 'color6 ok')
    equal(ruleSet.getRuleByName('color7').fixedValue, '#ABCDEF', 'color7 ok')
    equal(ruleSet.getRuleByName('color8').fixedValue, '#ABCDEF', 'color8 ok')
    equal(ruleSet.getRuleByName('color9').fixedValue, '#FFF', 'color9 ok')
    equal(ruleSet.getRuleByName('color10').fixedValue, '#FFF', 'color10 ok')
