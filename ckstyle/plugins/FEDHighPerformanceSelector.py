#/usr/bin/python
#encoding=utf-8

from .Base import *
from .helper import isHTMLTag

class FEDHighPerformanceSelector(RuleSetChecker):
    
    '''{
        "summary":"针对低性能的选择器的检查",
        "desc":"低性能选择器，害人害己还集体，本工具收集了一些低性能选择器的情形，具体请参见：<br>
            <code>FEDHighPerformanceSelector.py</code>中的相关内容"
    }'''

    def __init__(self):
        self.id = 'high-perf-selector'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_shorter = 'please shorter the selector "${selector}"'
        self.errorMsg_no1 = 'do not use low performance selector ">" in "${selector}"'
        self.errorMsg_lessTag = 'use less tag in "${selector}"'
        self.errorMsg_id = 'should not put "HTMLtag" and "#id" together in "${selector}"'
        self.errorMsg_class = 'should not put "HTMLtag" and ".class" together in "${selector}"'
        self.errorMsg_reg = 'should not use ~=,^=,|=,$=,*= in selector of "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        selectors = ruleSet.selector.replace('  ', '').split(',')
        for s in selectors:
            if s.find('@media') != -1:
                continue

            if s.find('=') != -1:
                if s.find('~=') != -1 or s.find('^=') != -1 or s.find('|=') != -1 or s.find('$=') != -1 or s.find('*=') != -1:
                    self.errorMsg = self.errorMsg_reg
                    return False

            splited = s.split(' ')
            if len(splited) > 5:
                self.errorMsg = self.errorMsg_shorter
                return False
            counter = 0
            for p in splited:
                if p == '>':
                    self.errorMsg = self.errorMsg_no1
                    return False

                innerSplit = p.split('#')
                if len(innerSplit) == 2 and isHTMLTag(innerSplit[0]):
                    self.errorMsg = self.errorMsg_id
                    return False

                innerSplit = p.split('.')
                if len(innerSplit) == 2 and isHTMLTag(innerSplit[0]):
                    self.errorMsg = self.errorMsg_class
                    return False

                if isHTMLTag(p):
                    counter = counter + 1
            if counter > 1:
                self.errorMsg = self.errorMsg_lessTag
                return False

        noSpace = ruleSet.selector.replace(' ', '')
        if noSpace.find('ulli') != -1 or noSpace.find('olli') != -1 or noSpace.find('dldt') != -1 or noSpace.find('dldd') != -1:
            self.errorMsg = self.errorMsg_lessTag
            return False
        return True
