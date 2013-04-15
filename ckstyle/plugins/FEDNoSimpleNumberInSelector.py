#/usr/bin/python
#encoding=utf-8

from .Base import *
import re
pattern = re.compile('\d+')

class FEDNoSimpleNumberInSelector(RuleSetChecker):
    
    '''{
        "summary":"不要在选择器中使用简单数字",
        "desc":"在业务代码的css中，选择器中不要使用简单的 <code>1, 2, 3</code> 来进行命名，下面的命名方式就是错误的：<br>
            <code>.test1</code> <code>.main1</code>，但是允许使用 <code>v1</code> <code>step1</code> <code>item1</code> 
            来代表版本、步骤、第几个元素的意思"
    }'''

    def __init__(self):
        self.id = 'number-in-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'do not simply use 1,2,3 as selector(use v1/step1/item1), in "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector

        if selector.find('@media') != -1:
            return True
            
        found = pattern.findall(selector)
        for x in found:
            if selector.find('v' + x) == -1 and selector.find('step' + x) == -1  and selector.find('item' + x) == -1 and selector.find('h' + x) == -1 :
                return False
        return True 
