#/usr/bin/python
#encoding=utf-8

from Base import *
import re

pattern = re.compile(r'(0\s*[\w]+)')
replacer = re.compile(',\s+')

class FEDNoUnitAfterZero(RuleChecker):
    
    '''{
        "summary":"xxx",
        "desc":"xxx"
    }'''

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

            if matched is None:
                continue

            for m in matched:
                if m != '0s':
                    return False

        return True 

    def fix(self, rule, config):
        if rule.name == 'expression':
            return

        fixed = rule.fixedValue
        rule.fixedValue = rule.fixedValue.replace(',', ', ')

        collector = []
        for v in rule.fixedValue.split(' '):
            v = v.strip()
            if v.find('(') != -1:
                matched = self._startsWithZero(v.split('(')[1])
            else:
                matched = self._startsWithZero(v)

            if matched is None:
                collector.append(v)
                continue

            finalV = v;
            for m in matched:
                if m != '0s':
                    finalV = finalV.replace(m, '0')
            collector.append(finalV)

        rule.fixedValue = replacer.sub(', ', ' '.join(collector))

    def _startsWithZero(self, value):
        matcher = pattern.match(value)
        if matcher is not None:
            return matcher.groups()
        return None
