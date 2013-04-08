#/usr/bin/python
#encoding=utf-8
from BinaryRule import *
from Hacks import doRuleDetect, doRuleSetDetect

class Browser():

    @staticmethod
    def handleRule(rule):
        rule.browser = doRuleDetect(rule.fixedName.strip(), rule.fixedValue.strip())

    @staticmethod
    def handleRuleSet(ruleSet):
        ruleSet.browser = doRuleSetDetect(ruleSet.selector.replace(' ', ''))
    
    @staticmethod
    def handleNestedStatement(ruleSet):
        pass