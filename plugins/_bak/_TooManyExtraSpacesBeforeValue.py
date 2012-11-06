from Base import *

class TooManyExtraSpacesBeforeValue(RuleChecker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = 'two many "space"s before "${value}" '
    def check(self, rule):
        ruleSet = rule.getRuleSet()
        if rule.roughValue.startswith('  '):
            return False
        return True 
