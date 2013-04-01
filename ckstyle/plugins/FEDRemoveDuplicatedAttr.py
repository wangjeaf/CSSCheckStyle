#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDRemoveDuplicatedAttr(RuleSetChecker):
    
    '''{
        "summary":"删除重复的属性设置",
        "desc":"如果在一个规则集中，对相同的两个属性进行了赋值，而且取值相同，则可以删除前面的赋值，例如：
            <br>
            <code>.test {</code><br>
            <code>&nbsp;&nbsp;&nbsp;&nbsp;width: 100px;</code><br>
            <code>&nbsp;&nbsp;&nbsp;&nbsp;width: 100px;</code><br>
            <code>}</code><br>
            <code>==></code><br>
            <code>.test {</code><br>
            <code>&nbsp;&nbsp;&nbsp;&nbsp;width: 100px;</code><br>
            <code>}</code>"
    }'''

    def __init__(self):
        self.id = 'remove-duplicated-attr'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'has more than 1 ${name} in "${selector}"'

    def check(self, ruleSet, config):
        rules = ruleSet.getRules()
        collector = []
        for rule in rules:
            info = self.ruleInfo(rule)
            if info in collector:
                return False
            collector.append(info)
        return True

    def fix(self, ruleSet, config):
        # make sure we use the last statement, so reverse and filter and reverse again
        # [a1, a2, b, c] ==> [c, b, a2, a1] ==> [c, b, a2] ==> [a2, b, c]
        rules = ruleSet.getRules()
        rules.reverse()
        newRules = []
        collector = []
        for rule in rules:
            info = self.ruleInfo(rule)
            if not info in collector:
                collector.append(info)
                newRules.append(rule)
        newRules.reverse()
        ruleSet.setRules(newRules)

    def ruleInfo(self, rule):
        if rule.fixedName != '':
            return rule.fixedName + ':' + rule.fixedValue
        return rule.strippedName + ':' + rule.strippedValue
