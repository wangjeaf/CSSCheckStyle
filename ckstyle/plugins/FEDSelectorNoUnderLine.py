from Base import *

class FEDSelectorNoUnderLine(RuleSetChecker):
    def __init__(self):
        self.id = 'no-underline-in-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'should not use _ in selector "${selector}"'

    def check(self, ruleSet):
        selector = ruleSet.selector
        if selector.find('_') != -1:
            return False
        return True 
