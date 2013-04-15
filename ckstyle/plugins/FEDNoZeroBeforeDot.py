#/usr/bin/python
#encoding=utf-8

from .Base import *

class FEDNoZeroBeforeDot(RuleChecker):
    
    '''{
        "summary":"删除0.x前面的0",
        "desc":" 0.xxx 前面的 0 是可以删除的，以实现更好的压缩。例如<br>
            <code>0.3px ==> .3px</code><br><br>
            <code>rgba(0,0,0,0.3)<code><br>
            <code>==></code><br>
            <code>rgba(0,0,0,.3)</code>"
    }'''

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
