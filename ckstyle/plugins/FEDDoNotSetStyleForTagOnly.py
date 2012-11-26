from Base import *
from helper import isHTMLTag
class FEDDoNotSetStyleForTagOnly(RuleSetChecker):
    def __init__(self):
        self.id = 'no-style-for-tag'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'should not set style for html tag in "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector.lower()
        if selector.find('@media') != -1:
            return True
        if selector.find('@-moz-document') != -1:
            return True
        selectors = selector.split(',')
        for s in selectors:
            if isHTMLTag(s.strip()):
                return False
        return True 
