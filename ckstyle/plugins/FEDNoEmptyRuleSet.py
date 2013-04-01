#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDNoEmptyRuleSet(RuleSetChecker):
    
    '''{
        "summary":"删除空的规则",
        "desc":"空的CSS规则集是没有任何意义的，应该直接删除掉"
    }'''

    def __init__(self):
        self.id = 'no-empty-ruleset'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'empty ruleset found "${selector}"'

    def check(self, ruleSet, config):
        if len(ruleSet.getRules()) == 0:
            return False
        return True 

    def fix(self, ruleSet, config):
        if len(ruleSet.getRules()) == 0:
            styleSheet = ruleSet.getStyleSheet()
            styleSheet.removeRuleSet(ruleSet)
