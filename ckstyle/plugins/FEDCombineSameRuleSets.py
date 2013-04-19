#/usr/bin/python
#encoding=utf-8

from .Base import *
from .helper import hasHackChars
from ckstyle.browsers.BinaryRule import ALL, STD
from ckstyle.browsers.Detector import doRuleSetDetect
class FEDCombineSameRuleSets(StyleSheetChecker):

    '''{
        "summary":"合并两个完全相同的规则集",
        "desc":"如果两个规则集完全一样，则可以进行合并。<br>
            需要指出的是：合并可能会带来功能上的问题。如果有问题，还请告知~<br>
            例如：<br>
            <code>.a {width:100px}</code><br>
            <code>.b {width:100px}</code><br>
            <code>==></code><br>
            <code>.a, .b {width:100px}</code><br>
            <br>
            <strong>安全模式下将不执行此规则</strong><br>
        "
    }'''

    def __init__(self):
        self.id = 'combine-same-rulesets'
        self.errorMsg_empty = '"%s" and "%s" contains same rules, should be combined in ${file}"'
        self.errorMsg = ''
        self.errorLevel = ERROR_LEVEL.ERROR

    # can be checked correctly only after reorder/fix/compress, so do not check
    def check(self, styleSheet, config):
        return True 

    def fix(self, styleSheet, config):
        browser = config._curBrowser if config._curBrowser is not None else ALL
        ruleSets = styleSheet.getRuleSets()
        mapping = self._gen_hash(ruleSets, browser)

        length = len(mapping)

        splitedSelectors = []
        for i in range(length):
            splitedSelectors.append([x.strip() for x in mapping[i][0].split(',') if x.strip() is not ''])

        for i in range(length):            
            if mapping[i][0] == 'extra':
                continue
            selectorHistory = []

            for j in range(i + 1, length):
                if mapping[i][1] != mapping[j][1]:
                    selectorHistory.extend(splitedSelectors[j])
                    continue

                # 合并则遵循如下策略：
                # 1、两者必须都与当前要求的浏览器兼容，即 browserI & browser != 0 and browserJ & browser != 0
                # 2、两者的浏览器兼容性必须完全一致，即 browserI ^ browserJ == 0
                # 第二点主要是因为有的属性合并以后，由于兼容性不同，受不兼容的selector影响，使本应该兼容的selector失效。
                browserI = doRuleSetDetect(mapping[i][0])
                browserJ = doRuleSetDetect(mapping[j][0])
                if not (browserI & browser != 0 and browserJ & browser != 0 and browserI ^ browserJ == 0):
                    continue

                # bakcground-position is dangerous, position设置必须在background-image之后
                if mapping[j][1].find('background-position') != -1:
                    selectorHistory.extend(splitedSelectors[j])
                    continue

                hasFlag = False
                # ".a {width:0} .a, .b{width:1}, .b{width:0}" 不应该被合并成 ".a, .b{width:0} .a, .b{width:1}"
                # 但是目前还有一个最严重的问题：
                # .c {width:1}, .d{width:0}, .b{width:1}, .a{width:0}
                # class="a c" => width 0
                # class="b d" => width 1
                # 一旦合并成 .b,.c{width:1} .d,.a{width:0} （不论往前合并还是往后合并，都是这个结果，囧）
                # class="a c" => width 0
                # class="b d" => width 0(本来为1)
                # 这是无法解决的问题，因为我不能在没有分析DOM的情况下，确定两个selector指向同一个dom
                # 为此，安全模式 --safeMode 诞生。
                for x in splitedSelectors[j]:
                    if x in selectorHistory:
                        hasFlag = True
                        break
                if hasFlag:
                    selectorHistory.extend(splitedSelectors[j])
                    continue

                # make it different
                mapping[j][1] = str(i) + str(j)
                mapping[j][0] = 'extra'

                # extend target selector
                target = styleSheet.getRuleSets()[i]
                src = styleSheet.getRuleSets()[j]
                target.extendSelector(src)

                # remove rule set
                styleSheet.removeRuleSetByIndex(j)
                selectorHistory.extend(splitedSelectors[j])

        # remember to clean after remove ruleset
        styleSheet.clean()

    def _gen_hash(self, ruleSets, browser):
        mapping = []
        counter = 0
        for r in ruleSets:
            if r.extra:# or doRuleSetDetect(r.selector) != STD:
                # make it impossible to equal
                mapping.append(['extra', "do_not_combine_" + str(counter)])
                counter = counter + 1
                continue
            mapping.append([r.selector, r.compressRules(browser)])
        return mapping
