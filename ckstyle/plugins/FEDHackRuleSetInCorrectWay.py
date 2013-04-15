#/usr/bin/python
#encoding=utf-8

from .Base import *

class FEDHackRuleSetInCorrectWay(ExtraChecker):
    
    '''{
        "summary":"hack规则时的检查",
        "desc":"针对Firefox Opera Safari等浏览器的 hack 方式， <strong>人人FED CSS编码规范</strong>中有详细的描述， 
            不允许使用规定之外的方式进行规则级别的hack"
    }'''

    def __init__(self):
        self.id = 'hack-ruleset'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'not correct hacking way in "${selector}"'

    def check(self, ruleSet, config):
        if not ruleSet.nested:
            return True

        selector = ruleSet.selector.strip()
        if selector.find('@-moz-document') != -1:
            if selector != '@-moz-document url-prefix()':
                return False

        if selector.find('-webkit-min-device-pixel-ratio:0') != -1:
            if selector != '@media screen and (-webkit-min-device-pixel-ratio:0)' and selector.find('-webkit-min-device-pixel-ratio:10000') == -1:
                return False

        if selector.find('-webkit-min-device-pixel-ratio:10000') != -1:
            if selector.find('@media all') == -1 or selector.find('not all and') == -1 or selector.find('-webkit-min-device-pixel-ratio:0') == -1:
                return False

        return True 
