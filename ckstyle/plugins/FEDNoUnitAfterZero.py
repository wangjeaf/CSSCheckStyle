#/usr/bin/python
#encoding=utf-8

from Base import *
import re

pattern_unit = re.compile(r'(0\s*[\w]+)')
replacer_unit = re.compile(',\s+')

class FEDNoUnitAfterZero(RuleChecker):
    
    '''{
        "summary":"删除0后面的单位",
        "desc":"0后面的单位可以删除，以实现更好的压缩。比如 <code>0px ==> 0</code> ，<code>0em ==> 0</code> 等，
            但是<code>transition: 0s</code>的<code>s</code>不能省略"
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

        rule.fixedValue = replacer_unit.sub(', ', ' '.join(collector))

    def _startsWithZero(self, value):
        matcher = pattern_unit.match(value)
        if matcher is not None:
            return matcher.groups()
        return None
