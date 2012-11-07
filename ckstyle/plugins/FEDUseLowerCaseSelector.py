from Base import *

class FEDUseLowerCaseSelector(RuleSetChecker):
    def __init__(self):
        self.id = 'lowercase-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'selector should use lower case, in "${selector}"'

    def check(self, rule):
        selector = rule.selector
        if selector.lower() != selector:
            return False

        return True 
