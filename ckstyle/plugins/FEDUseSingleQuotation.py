#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDUseSingleQuotation(RuleChecker):
    
    '''{
        "summary":"使用单引号",
        "desc":"CSS的属性取值一律使用单引号<code>'</code>， 不允许使用双引号"
    }'''

    def __init__(self):
        self.id = 'single-quotation'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'replace " with \' in "${selector}"'

    def check(self, rule, config):
        if self._findDouble(rule.value):
            return False

        return True

    def fix(self, rule, config):
        if self._findDouble(rule.value):
            rule.fixedValue = rule.value.replace('"', "'")

    def _findDouble(self, value):
        return value.find('"') != -1
