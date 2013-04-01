#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDFixCommentInValue(RuleChecker):
    
    '''{
        "summary":"修复属性中的注释",
        "desc":"width:/* fdasfdas */ 100px /* fdafdas */; ==> width:100px;"
    }'''

    def __init__(self):
        self.id = 'fix-comment-in-value'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = ''
        self.private = True

    def check(self, rule, config):
        return True


    def fix(self, rule, config):
        if rule.name == 'expression':
            return
        value = rule.fixedValue
        if value.find('/*') == -1:
            return

        splited = value.split('/*')
        collector = []
        for x in splited:
            tmp = x.split('*/')
            if len(tmp) == 1:
                collector.append(tmp[0])
            else:
                collector.append(tmp[1])
        rule.fixedValue = ''.join(collector)
