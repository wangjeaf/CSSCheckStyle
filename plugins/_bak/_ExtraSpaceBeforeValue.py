from Base import *

class ExtraSpaceBeforeValue(RuleChecker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = 'need "extra space" before "${value}" '
    def check(self, rule):
        ruleSet = rule.getRuleSet()
        if not ruleSet.getSingleLineFlag() and not rule.roughValue.startswith(' '):
            return False
        return True 
