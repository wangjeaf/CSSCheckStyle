#/usr/bin/python
#encoding=utf-8

from .Base import *
from .helper import isCss3PrefixProp

class FEDHackAttributeInCorrectWay(RuleChecker):
    
    '''{
        "summary":"hack属性时的检查",
        "desc":"必须使用正确的 hack 方式， 比如 <code>_ * +</code> 等，其他的属性前缀一律不允许"
    }'''

    def __init__(self):
        self.id = 'hack-prop'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = '"${name}" is not in correct hacking way in "${selector}"'

    def check(self, rule, config):
        if rule.value.find(r'\0') != -1:
            return False

        stripped = rule.roughName.strip()
        if rule.name == stripped.lower():
            return True

        if isCss3PrefixProp(rule.name):
            return True

        if not stripped.startswith('_') and not stripped.startswith('*') and not stripped.startswith('+'):
            return False

        return True 
