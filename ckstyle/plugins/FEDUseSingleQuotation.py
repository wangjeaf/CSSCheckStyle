from Base import *

class FEDUseSingleQuotation(RuleChecker):
    def __init__(self):
        self.id = 'single-quotation'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'replace " with \' in "${selector}"'

    def check(self, rule):
        if self._findDouble(rule.value):
            return False

        return True

    def fix(self, rule):
        if self._findDouble(rule.value):
            rule.fixedValue = rule.value.replace('"', "'")

    def _findDouble(self, value):
        return value.find('"') != -1
