from Base import *
from helper import isSimpleSelector

class FEDDoNotSetStyleForSimpleSelector(RuleSetChecker):
    def __init__(self):
        self.id = 'no-style-for-simple-selector'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_rough = 'should not set style for "%s" in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        selector = ruleSet.selector.lower()

        if selector.find('@media') != -1:
            return True

        if selector.find('@-moz-document') != -1:
            return True

        selectors = selector.split(',')
        for s in selectors:
            s = s.strip()
            if isSimpleSelector(s):
                self.errorMsg = self.errorMsg_rough % s
                return False
        return True 
