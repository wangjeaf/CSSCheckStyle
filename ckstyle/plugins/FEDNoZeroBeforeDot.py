from Base import *

class FEDNoZeroBeforeDot(RuleChecker):
    def __init__(self):
        self.id = 'no-zero-before-dot'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'zero should be removed when meet 0.xxx in "${selector}"'

    def check(self, rule, config):
        value = rule.value

        if self._startsWithZeroDot(value):
            return False

        values = rule.value.split(' ')
        for v in values:
            if self._startsWithZeroDot(v.strip()):
                return False

        return True 

    def fix(self, rule, config):
        fixedValue = rule.fixedValue
        for v in fixedValue.split(' '):
            if self._startsWithZeroDot(v):
                rule.fixedValue = rule.fixedValue.replace(v, v[1:])

    def _startsWithZeroDot(self, value):
        return value.startswith('0.')
