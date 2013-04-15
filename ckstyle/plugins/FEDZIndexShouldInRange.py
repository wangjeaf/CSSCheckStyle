#/usr/bin/python
#encoding=utf-8

from .Base import *
import string
from .helper import isCss3PrefixProp

class FEDZIndexShouldInRange(RuleChecker):
    
    '''{
        "summary":"z-index取值应符合范围要求",
        "desc":"<code>z-index</code> 的取值如果混乱，则会造成层之间的相互覆盖，
            因此 <code>z-index</code> 取值必须符合一定的范围要求，具体要求请参见人人FED CSS编码规范"
    }'''

    def __init__(self):
        self.id = 'z-index-in-range'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'value of "z-index" is not correct in "${selector}"'

    def check(self, rule, config):
        if rule.name != 'z-index':
            return True

        zIndex = None
        try:
            zIndex = string.atoi(rule.value)
        except ValueError:
            return False

        if zIndex < -1:
            return False

        if zIndex > 2100:
            return False

        return True 
