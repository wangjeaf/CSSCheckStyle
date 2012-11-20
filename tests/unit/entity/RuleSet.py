from helper import *

def doTest():
    _ruleSet()

def _ruleSet():
    ruleSet = RuleSet('   .test ', '  width:100px;height:100px;  ', '/* aa */   ', None)
    equal(ruleSet.selector, '.test', 'selector is ok')
    equal(ruleSet.roughSelector, '   .test ', 'roughSelector is ok')
    equal(ruleSet.roughValue, '  width:100px;height:100px;  ', 'roughValue is ok')
    equal(ruleSet.roughComment, '/* aa */   ', 'rough comment is ok')
    equal(ruleSet.values, 'width:100px;height:100px;', 'values is ok')
    ok(ruleSet.singleLineFlag, 'it is single line')
    ok(ruleSet.getSingleLineFlag(), 'it is single line')
    equal(ruleSet.getStyleSheet(), None, 'no stylesheet')

    equal(len(ruleSet.getRules()), 0, 'no rules')
    equal(ruleSet.indexOf('width'), -1, 'no _width')
    equal(ruleSet.existNames('width'), False, 'no width again')
    equal(ruleSet.existNames('  _width '), False, 'no rough _width')
    equal(ruleSet.getRuleByName('width'), None, 'can not find width')
    equal(ruleSet.getRuleByRoughName('  _width '), None, 'can not find _width')

    ruleSet.addRuleByStr(' .aaa', '  _width ', ' 100px; ')
    
    equal(len(ruleSet.getRules()), 1, 'one rule')
    equal(ruleSet.indexOf('_width'), 0, 'found width')
    equal(ruleSet.existNames('width'), True, 'found width again')
    equal(ruleSet.existRoughNames('  _width '), True, 'found rough width')
    equal(ruleSet.getRuleByName('width').value, '100px', 'find width')
    equal(ruleSet.getRuleByRoughName('  _width ').value, '100px', 'find width by rough name')
    equal(ruleSet.getRuleByStrippedName('_width').value, '100px', 'find width by stripped name')

    ruleSet.addRuleByStr(' .aaa', 'height', '100px; ')
    equal(len(ruleSet.getRules()), 2, 'two rules')
    equal(ruleSet.getRules()[0].name, 'width', 'width is first')
    equal(ruleSet.getRules()[1].name, 'height', 'height is second')
