from helper import *


def doTest():
    fixer = doFix("a.feed-back-v6 { display: block; position: fixed; _position: absolute; top: 155px; _top: expression(documentElement.scrollTop + 'px'); _margin-top: 155px; right: 0; padding: 10px; font-size: 14px; font-weight: bold; width: 1em; background: #F7F7FF; z-index: 1999; }", '')

    equal(fixer.doCompress(), "a.feed-back-v6{display:block;position:fixed;_position:absolute;top:155px;_top:expression(documentElement.scrollTop + 'px');right:0;width:1em;_margin-top:155px;padding:10px;background:#F7F7FF;font-size:14px;font-weight:bold;z-index:1999}", 'compress feed-back-v6 is ok')

    styleSheet = fixer.getStyleSheet()
    equal(len(styleSheet.getRuleSets()), 1, 'one ruleset')
    ruleSet = styleSheet.getRuleSets()[0]
    equal(ruleSet.selector, 'a.feed-back-v6', 'yes it is a.feed-back-v6')

    rules = ruleSet.getRules()
    equal(rules[0].name, 'display', 'element name is ok')
    equal(rules[1].name, 'position', 'element name is ok')
    equal(rules[2].name, 'position', 'element name is ok')
    equal(rules[3].name, 'top', 'element name is ok')
    equal(rules[4].name, 'top', 'element name is ok')
    equal(rules[5].name, 'right', 'element name is ok')
    equal(rules[6].name, 'width', 'element name is ok')
    equal(rules[7].name, 'margin-top', 'element name is ok')
    equal(rules[8].name, 'padding', 'element name is ok')
    equal(rules[9].name, 'background', 'element name is ok')
    equal(rules[10].name, 'font-size', 'element name is ok')
    equal(rules[11].name, 'font-weight', 'element name is ok')
    equal(rules[12].name, 'z-index', 'element name is ok')
