#/usr/bin/python
#encoding=utf-8

from Base import *
from validators.ValidatorFactory import doValidate

class FEDUseValidValues(RuleChecker):
    
    '''{
        "summary":"不正确的属性取值",
        "desc":"检查不正确的属性取值，比如： <code>width: underline;</code> 等"
    }'''

    def __init__(self):
        self.id = 'valid-values'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_rough = '%s in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        flag, msg = doValidate(rule.name, rule.strippedValue)
        if flag is True:
            return True

        self.errorMsg = self.errorMsg_rough % msg
        return False

    def fix(self, rule, config):
        pass
