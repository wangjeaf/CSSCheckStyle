from Base import *
import re

pattern = re.compile(r'(0\s*[\w]+)')

class FEDNoUnitAfterZero(RuleChecker):
    def __init__(self):
        self.id = 'del-unit-after-zero'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'unit should be removed when meet 0 in "${selector}"'

    def check(self, rule, config):

        values = rule.value.split(' ')
        for v in values:
            v = v.strip()
            if v.find('(') != -1:
                matched = self._startsWithZero(v.split('(')[1])
            else:
                matched = self._startsWithZero(v)

            if matched is not None:
                return False

        return True 

    def fix(self, rule, config):
        fixed = rule.fixedValue

        collector = []
        for v in rule.fixedValue.split(' '):
            v = v.strip()
            if v.find('(') != -1:
                matched = self._startsWithZero(v.split('(')[1])
            else:
                matched = self._startsWithZero(v)

            if matched is not None:
                collector.append(v.replace(matched, '0'))
            else:
                collector.append(v)

        rule.fixedValue = ' '.join(collector)

    def _startsWithZero(self, value):
        matcher = pattern.match(value)
        if matcher is not None:
            return matcher.group()
        return None
