#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isCssProp

class FEDUnknownCssNameChecker(RuleChecker):
    
    '''{
        "summary":"错误的css属性",
        "desc":"本工具会帮您查找错误的CSS属性，如果写错了，即可收到错误提示"
    }'''

    def __init__(self):
        self.id = 'unknown-css-prop'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'unknown attribute name "${name}" found in "${selector}"'

    def check(self, rule, config):
        return isCssProp(rule.name.lower())
