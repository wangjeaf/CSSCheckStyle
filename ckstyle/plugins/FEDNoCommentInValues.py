from Base import *

class FEDNoCommentInValues(RuleSetChecker):
    def __init__(self):
        self.id = 'no-comment-in-value'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = 'find css comment (/* */) in "${selector}"'

    def check(self, ruleSet, config):
        if ruleSet.roughValue.find('/*') != -1 or ruleSet.roughValue.find('*/') != -1:
            return False
        return True 
