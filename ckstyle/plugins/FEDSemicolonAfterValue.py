from Base import *

class FEDSemicolonAfterValue(RuleChecker):
    def __init__(self):
        self.id = 'add-semicolon'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'each rule in "${selector}" need semicolon in the end, "${name}" has not'

    def check(self, rule, config):
        if not rule.roughValue.strip().endswith(';'):
            return False
        return True 
