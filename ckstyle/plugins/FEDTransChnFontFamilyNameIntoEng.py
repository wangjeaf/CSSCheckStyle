#/usr/bin/python
#encoding=utf-8

from .Base import *
from .helper import containsChnChar

class FEDTransChnFontFamilyNameIntoEng(RuleChecker):
    
    '''{
        "summary":"字体设置时使用英文",
        "desc":"有的字体设置可以通过中文和英文两者方式来声明，比如<br>
            <code>微软雅黑</code> 和 <code>Microsoft Yahei</code> ，我们推荐用英文的方式来实现"
    }'''

    def __init__(self):
        self.id = 'no-chn-font-family'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'should not use chinese font family name in "${selector}"'

    def check(self, rule, config):
        if rule.name != 'font' and rule.name != 'font-family':
            return True

        if containsChnChar(rule.value):
            return False

        return True 
