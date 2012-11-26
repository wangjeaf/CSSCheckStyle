from Base import *

class FEDNoZeroBeforeDot(RuleChecker):
    def __init__(self):
        self.id = 'no-zero-before-dot'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'zero should be removed when meet 0.xxx in "${selector}"'

    def check(self, rule, config):
        value = rule.value

        def startsWithZeroDot(value):
            return value.startswith('0.')

        if startsWithZeroDot(value):
            return False

        values = rule.value.split(' ')
        for v in values:
            if startsWithZeroDot(v.strip()):
                return False

        return True 
