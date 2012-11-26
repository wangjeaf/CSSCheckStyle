from Base import *

class FEDUseLowerCaseSelector(RuleSetChecker):
    def __init__(self):
        self.id = 'lowercase-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'selector should use lower case, in "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector
        if selector.lower() != selector:
            return False

        return True 

    def fix(self, ruleSet, config):
        selector = ruleSet.selector
        if selector.lower() != selector:
            ruleSet.fixedSelector = ruleSet.fixedSelector.lower()
