#/usr/bin/python
#encoding=utf-8

from .helper import getAttrOrder
from .Base import *

class FEDStyleShouldInOrder(RuleSetChecker):
    
    '''{
        "summary":"属性应该按照推荐的顺序编写",
        "desc":"相同的CSS属性，如果按照推荐的顺序来编写，浏览器的处理性能会更高，推荐的顺序一般为：<br>
            显示属性 => 盒模型属性 => 背景/行高 => 文本属性 => 其他"
    }'''

    def __init__(self):
        self.id = 'keep-in-order'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_rough = '"%s" should after "%s" in "${selector}" (order: display/box/text/other/css3)'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        rules = ruleSet.getRules()
        if len(rules) < 2:
            return True

        order = self._generateNameOrderMapping(rules)
        length = len(order)
        for i in range(length):
            if i == length - 1:
                break;
            current = order[i]
            nextAttr = order[i + 1]

            if current[0] > nextAttr[0]:
                self.errorMsg = self.errorMsg_rough % (current[1], nextAttr[1])
                return False

        return True 

    def fix(self, ruleSet, config):
        rules = ruleSet.getRules()
        if len(rules) < 2:
            return True

        def comp(a, b):
            return a[0] - b[0]

        mapping = self._generateNameRuleMapping(rules)
        mapping.sort(comp)
        sortedRules = []
        for x in range(len(mapping)):
            sortedRules.append(mapping[x][1])
        ruleSet.setRules(sortedRules)

    def _generateNameOrderMapping(self, rules):
        return [(getAttrOrder(rule.name, rule.strippedName), rule.strippedName) for rule in rules]

    def _generateNameRuleMapping(self, rules):
        return [(getAttrOrder(rule.name, rule.strippedName), rule) for rule in rules]
