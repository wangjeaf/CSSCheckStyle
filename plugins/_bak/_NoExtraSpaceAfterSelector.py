from Base import *

class NoExtraSpaceAfterSelector(RuleSetChecker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = 'should have "extra space" at the end of "${selector}"'

    def check(self, ruleSet):
        selector = ruleSet.roughSelector

        if not selector.endswith(' '):
            return False

        if ruleSet.roughSelector.endswith('  '):
            return False

        return True 
