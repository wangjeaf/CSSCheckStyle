#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isSimpleSelector

class FEDDoNotSetStyleForSimpleSelector(RuleSetChecker):
    
    '''{
        "summary":"不要为简单选择器设置样式",
        "desc":"一些简单的选择器，比如：<br>
            <code>.nav/.list/.content</code><br>
            非常容易造成属性的相互覆盖，因此在写这样的选择器时，最好加上前缀，比如<br>
            <code>.module-name .nav</code><br><br>
            工具现有的简单选择器判断，请参考：<br>
            <code>plugins/helper.py</code>"
    }'''

    def __init__(self):
        self.id = 'no-style-for-simple-selector'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_rough = 'should not set style for "%s" in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        selector = ruleSet.selector.lower()

        if selector.find('@media') != -1:
            return True

        if selector.find('@-moz-document') != -1:
            return True

        selectors = selector.split(',')
        for s in selectors:
            s = s.strip()
            if isSimpleSelector(s):
                self.errorMsg = self.errorMsg_rough % s
                return False
        return True 
