#/usr/bin/python
#encoding=utf-8

from .Base import *

class FEDFixOutlineZero(RuleChecker):
    
    '''{
        "summary":"修复outline:none",
        "desc":"<code>outline:none</code> 和 <code>outline:0</code> 实现了相同的功能，但是后者的代码更简洁，便于压缩。"
    }'''

    def __init__(self):
        self.id = 'outline-zero'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = ''

    def check(self, rule, config):
        return True

    def fix(self, rule, config):
        if rule.name == 'outline' and rule.fixedValue == 'none':
            rule.fixedValue = '0'