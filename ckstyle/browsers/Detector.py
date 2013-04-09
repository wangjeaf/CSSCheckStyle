#/usr/bin/python
#encoding=utf-8
from BinaryRule import *
from Hacks import doRuleDetect, doRuleSetDetect, doExtraDetect

class Browser():

    @staticmethod
    def handleRule(rule):
        rule.browser = doRuleDetect(rule.fixedName, rule.fixedValue)

    @staticmethod
    def handleRuleSet(ruleSet):
        ruleSet.browser = doRuleSetDetect(ruleSet.selector)
    
    @staticmethod
    def handleNestedStatement(statement):
    	statement.browser = doExtraDetect(statement.selector)