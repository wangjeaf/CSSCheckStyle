from Base import *

class ShouldNotSetStyleForBody(RuleSetChecker):
    def __init__(self):
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'should not set style for "body" in "${selector}"'
    def check(self, ruleSet):
        selector = ruleSet.selector
        selectors = selector.replace('\n', '').split(',')
        for s in selectors:
            if s.strip() == 'body':
                return False
        return True 
