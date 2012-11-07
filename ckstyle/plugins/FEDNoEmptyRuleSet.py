from Base import *

class FEDNoEmptyRuleSet(RuleSetChecker):
    def __init__(self):
        self.id = 'no-empty-ruleset'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'empty ruleset found "${selector}"'

    def check(self, ruleSet):
        if len(ruleSet.getRules()) == 0:
            return False
        return True 
