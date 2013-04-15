#/usr/bin/python
#encoding=utf-8

from .Base import *

class FEDSemicolonAfterValue(RuleChecker):
    
    '''{
        "summary":"为每一个属性后添加分号",
        "desc":"按照CSS编码规范，每一个规则后面都必须加上分号 <code>;</code>"
    }'''

    def __init__(self):
        self.id = 'add-semicolon'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'each rule in "${selector}" need semicolon in the end, "${name}" has not'

    def check(self, rule, config):
        if not rule.roughValue.strip().endswith(';'):
            return False
        return True 
