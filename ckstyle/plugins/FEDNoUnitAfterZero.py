from Base import *

class FEDNoUnitAfterZero(RuleChecker):
    def __init__(self):
        self.id = 'del-unit-after-zero'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'unit should be removed when meet 0 in "${selector}"'

    def check(self, rule):

        def startsWithZero(value):
            return value.startswith('0') and value != '0' and value[1] != '.'

        if startsWithZero(rule.value):
            return False

        values = rule.value.split(' ')
        for v in values:
            if startsWithZero(v.strip()):
                return False

        return True 
