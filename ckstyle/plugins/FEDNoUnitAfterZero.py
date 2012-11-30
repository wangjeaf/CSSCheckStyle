from Base import *

class FEDNoUnitAfterZero(RuleChecker):
    def __init__(self):
        self.id = 'del-unit-after-zero'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'unit should be removed when meet 0 in "${selector}"'

    def check(self, rule, config):

        values = rule.value.split(' ')
        for v in values:
            if self._startsWithZero(v.strip()):
                return False

        return True 

    def fix(self, rule, config):
        fixed = rule.fixedValue

        collector = []
        for v in rule.fixedValue.split(' '):
            v = v.strip()
            if self._startsWithZero(v):
                collector.append('0')
            else:
                collector.append(v)

        rule.fixedValue = ' '.join(collector)

    def _startsWithZero(self, value):
        return value.startswith('0') and value != '0' and value[1] != '.'
