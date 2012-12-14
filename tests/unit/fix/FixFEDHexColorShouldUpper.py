from helper import *

def doTest():
    _color()
    _complicated_color()
    _special()

def _complicated_color():
    fixer, msg = doFix('.test {background0:#dddddd url(dddddd) no-repeat left top;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.getRuleByName('background0').fixedValue, '#DDD url(dddddd) no-repeat left top', 'bgcolor 0 ok')
    
    fixer, msg = doFix('.test {border:1px solid #ffffff;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.getRuleByName('border').fixedValue, '1px solid #FFF', 'border is ok')

    fixer, msg = doFix('.test {border:1px solid red;}', '')
    styleSheet = fixer.getStyleSheet()
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.getRuleByName('border').fixedValue, '1px solid red', 'red border is ok')

def _color():
    fixer, msg = doFix('.test {color0:red;color1:#DDD;color2:#DDDDDD;color3:#dddddd;color4:#ddd;color5:#DDFFCC;color6:#ABCDEF;color7:#ABCDEFGH;color8:#abcdef;color9:#ffff;color10:#f;}', '')

    styleSheet = fixer.getStyleSheet()
    equal(len(styleSheet.getRuleSets()), 1, 'one ruleset')
    equal(len(styleSheet.getRuleSets()[0].getRules()), 11, 'eleven rules')

    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.getRuleByName('color0').fixedValue, 'red', 'color0 ok')
    equal(ruleSet.getRuleByName('color1').fixedValue, '#DDD', 'color1 ok')
    equal(ruleSet.getRuleByName('color2').fixedValue, '#DDD', 'color2 ok')
    equal(ruleSet.getRuleByName('color3').fixedValue, '#DDD', 'color3 ok')
    equal(ruleSet.getRuleByName('color4').fixedValue, '#DDD', 'color4 ok')
    equal(ruleSet.getRuleByName('color5').fixedValue, '#DFC', 'color5 ok')
    equal(ruleSet.getRuleByName('color6').fixedValue, '#ABCDEF', 'color6 ok')
    equal(ruleSet.getRuleByName('color7').fixedValue, '#ABCDEFGH', 'color7 ok')
    equal(ruleSet.getRuleByName('color8').fixedValue, '#ABCDEF', 'color8 ok')
    equal(ruleSet.getRuleByName('color9').fixedValue, '#FFF', 'color9 ok')
    equal(ruleSet.getRuleByName('color10').fixedValue, '#FFF', 'color10 ok')

def _special():
    css = '.t{box-shadow:0 4px 5px 1px rgba(74, 116, 161, 0.1), inset 0 -1px #cadaea, inset 0 -2px #fbfcfe;}'
    fixer, msg = doFix(css, '')
    ruleSet = fixer.getStyleSheet().getRuleSets()[0]
    rule = ruleSet.getRules()[0]
    equal(rule.fixedValue, '0 4px 5px 1px rgba(74, 116, 161, .1), inset 0 -1px #CADAEA, inset 0 -2px #FBFCFE', 'fixed ok')
