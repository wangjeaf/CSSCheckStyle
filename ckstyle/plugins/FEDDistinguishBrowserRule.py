#/usr/bin/python
#encoding=utf-8

from .Base import *
import string
from ckstyle.browsers.Detector import Browser

class FEDDistinguishBrowserRule(RuleChecker):
    
    '''{
        "summary":"在属性级别区分浏览器",
        "desc":"目的是针对不同的浏览器，生成不同的CSS"
    }'''

    def __init__(self):
        self.id = 'rule-for-browsers'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = ''

    def check(self, rule, config):
        return True

    def fix(self, rule, config):
        Browser.handleRule(rule)