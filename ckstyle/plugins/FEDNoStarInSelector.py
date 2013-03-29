#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDNoStarInSelector(RuleSetChecker):
    
    '''{
        "summary":"xxx",
        "desc":"xxx"
    }'''

    def __init__(self):
        self.id = 'no-star-in-selector'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'please remove low performance selector "*" from "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector
        if selector.find('*') == -1:
            return True

        replaced = selector.replace(' ', '')
        if replaced.startswith('*html') or replaced.startswith('*+html'):
            return True

        if replaced.find('*:not') != -1:
            return True

        # give it to FEDHighPerformanceSelector.py
        if replaced.find('*=') != -1 and len(replaced.split('*')) == 2:
            return True

        return False
