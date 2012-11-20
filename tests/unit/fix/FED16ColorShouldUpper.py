from helper import *

def doTest():
    fixer = doFix('.test {color1:#DDD;color2:#DDDDDD;color3:#abcdef;color4:#abc;color5:#DDFFCC;color6:#ABCDEF;color7:#ABCDEFGH}', '')

    styleSheet = fixer.getStyleSheet()
    equal(len(styleSheet.getRuleSets()), 1, 'one ruleset')
    equal(len(styleSheet.getRuleSets()[0].getRules()), 7, 'seven rules')
