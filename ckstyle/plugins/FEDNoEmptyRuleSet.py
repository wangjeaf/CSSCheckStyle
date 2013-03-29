#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDNoEmptyRuleSet(RuleSetChecker):
    
    '''{
        "summary":"xxx",
        "desc":"xxx"
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
