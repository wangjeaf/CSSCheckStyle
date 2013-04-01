#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDNoCommentInValues(RuleSetChecker):
    
    '''{
        "summary":"不要在css属性中添加注释",
        "desc":"CSS的注释应该写在 <code>selector</code> 前面，属性中不允许添加css注释，例如：<br>
            <code>.selector {</code><br>
            <code>&nbsp;&nbsp;&nbsp;&nbsp;width: 100px;/*comment here*/</code><br>
            <code>}</code>
        "
    }'''

    def __init__(self):
        self.id = 'no-comment-in-value'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = 'find css comment (/* */) in "${selector}"'

    def check(self, ruleSet, config):
        if ruleSet.roughValue.find('/*') != -1 or ruleSet.roughValue.find('*/') != -1:
            return False
        return True 
