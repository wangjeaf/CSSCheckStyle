from Base import *

class ExtraSpaceBeforeSelector(RuleSetChecker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = '"extra space" before "${selector}", maybe at the end of previous rule'

    def check(self, ruleSet):
        if ruleSet.roughSelector.replace('\n', '').startswith(' '):
            return False
        return True 
