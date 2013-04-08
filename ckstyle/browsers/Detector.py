#/usr/bin/python
#encoding=utf-8
from BinaryRule import *
from Hacks import doRuleDetect, doRuleSetDetect

class Browser():

    # http://www.swordair.com/tools/css-hack-table/
    # big table
    @staticmethod
    def handleRule(rule):
        rule.browser = doRuleDetect(rule.fixedName.strip(), rule.fixedValue.strip())

    @staticmethod
    def handleRuleSet(ruleSet):
        ruleSet.browser = doRuleSetDetect(ruleSet.selector.replace(' ', ''))
    
    @staticmethod
    def handleNestedStatement(ruleSet):
        pass