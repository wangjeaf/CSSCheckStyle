from helper import *

def doTest():
    _rule()
    _getRuleSet()

def _getRuleSet():
    ruleSet = RuleSet('.selector', 'width:100px;', '/* aa */', None)
    rule = Rule("", "", "", ruleSet)
    equal(rule.getRuleSet(), ruleSet, 'get rule set')
    equal(rule.getRuleSet().selector, '.selector', 'it is what I need')

def _rule():
    rule = Rule("   .test ", "  _width ", " 100px; ", None)
    equal(rule.selector, '.test', 'selector is ok')
    equal(rule.roughSelector, '   .test ', 'roughSelector is ok')
    equal(rule.roughName, '  _width ', 'roughName is ok')
    equal(rule.name, 'width', 'name is ok')
    equal(rule.roughValue, ' 100px; ', 'roughValue is ok')
    equal(rule.value, '100px', 'value is ok')
    equal(rule.strippedName, '_width', 'stripped name is ok')
    equal(rule.strippedValue, '100px;', 'strippedValue is ok')
