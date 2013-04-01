#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDNoExpression(RuleChecker):
    
    '''{
        "summary":"不要使用非一次性表达式",
        "desc":"IE下，非一次性expression对性能有很大的影响，或许一次鼠标移动，
            将触发<strong>成千上万次</strong>的expression表达式的执行，
            因此，为了浏览器的更新换代，应该杜绝使用非一次性表达式。<br>
            本工具针对一次性表达式的检查，将判断expression中是否有如下两个内容：<br>
            1. <code>Expressions</code><br>
            2. <code>this.style.attrName = </code>"
    }'''

    def __init__(self):
        self.id = 'no-expression'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_use = 'should not use expression in "${selector}" '
        self.errorMsg_hack = 'should add hack for expression in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        value = rule.value
        name = rule.name
        replaced = value.replace(' ', '')

        if value.find('expression') == -1:
            return True

        if replaced.find('Expressions') != -1 or replaced.find('this.style.' + name + '=') != -1 or replaced.find('this.runtimeStyle.' + name + '=') != -1:
            if rule.name == rule.strippedName:
                selector = rule.selector.replace(' ', '')
                if selector.find('*html') == -1:
                    self.errorMsg = self.errorMsg_hack
                    return False
            return True

        self.errorMsg = self.errorMsg_use
        return False
