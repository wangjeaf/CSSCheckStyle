from Base import *

class FEDNoSimpleNumberInSelector(RuleSetChecker):
    def __init__(self):
        self.id = 'number-in-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'do not simply use 1,2,3 as selector, in "${selector}"'

    def check(self, ruleSet):
        selector = ruleSet.selector

        if selector.find('@media') != -1:
            return True

        for x in range(9):
            x = str(x)
            if selector.find(x) != -1 and selector.find('v' + x) == -1 and selector.find('step' + x) == -1:
                return False
        return True 
