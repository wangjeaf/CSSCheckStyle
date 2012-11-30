from Base import *
from helper import isKeyFrames

class FEDNoEmptyRuleSet(RuleSetChecker):
    def __init__(self):
        self.id = 'no-empty-ruleset'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'empty ruleset found "${selector}"'

    def check(self, ruleSet, config):
        if isKeyFrames(ruleSet.selector):
            return True

        if len(ruleSet.getRules()) == 0:
            return False
        return True 

    def fix(self, ruleSet, config):
        if isKeyFrames(ruleSet.selector):
            return

        if len(ruleSet.getRules()) == 0:
            styleSheet = ruleSet.getStyleSheet()
            styleSheet.removeRuleSet(ruleSet)
