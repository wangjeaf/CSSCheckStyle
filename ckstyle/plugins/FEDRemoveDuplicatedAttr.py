#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDRemoveDuplicatedAttr(RuleSetChecker):
    
    '''{
        "summary":"xxx",
        "desc":"xxx"
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
