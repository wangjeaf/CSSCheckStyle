from Base import *

class ExtraSpaceAtTheEndOfRule(RuleSetChecker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = '"extra space" at the end of "${selector}"'

    def check(self, ruleSet):
        single = ruleSet.getSingleLineFlag()
        if single:
            return True
        if ruleSet.roughValue.replace('\n', '').endswith(' '):
            return False
        return True 
