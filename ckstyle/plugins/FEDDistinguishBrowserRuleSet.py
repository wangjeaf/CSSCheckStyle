#/usr/bin/python
#encoding=utf-8

from .Base import *
import string
from ckstyle.browsers.Detector import Browser

class FEDDistinguishBrowserRuleSet(RuleSetChecker):
    
    '''{
        "summary":"在规则集级别区分浏览器",
        "desc":"目的是针对不同的浏览器，生成不同的CSS规则集"
    }'''

    def __init__(self):
        self.id = 'ruleset-for-browsers'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = ''

    def check(self, ruleSet, config):
        return True

    def fix(self, ruleSet, config):
        Browser.handleRuleSet(ruleSet)