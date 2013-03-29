from Base import *

class FEDFixOutlineZero(RuleChecker):
    def __init__(self):
        self.id = 'outline-zero'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = ''

    def check(self, rule, config):
        return True

    def fix(self, rule, config):
        if rule.name == 'outline' and rule.fixedValue == 'none':
            rule.fixedValue = '0'