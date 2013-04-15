#/usr/bin/python
#encoding=utf-8

from .Base import *
from .helper import isFontFamilyName

class FEDCanNotSetFontFamily(RuleChecker):
    
    '''{
        "summary":"不允许业务代码设置字体",
        "desc":"由于业务代码中随意设置字体，导致字体取值混乱，因此不允许随意在业务代码中设置字体"
    }'''

    def __init__(self):
        self.id = 'no-font-family'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'can not set font-family for "${selector}"'

    def check(self, rule, config):
        if rule.name == 'font-family':
            return False

        if rule.name == 'font':
            # many fonts
            if rule.value.find(',') != -1:
                return False

            # one font
            splited = rule.value.split(' ')
            if isFontFamilyName(splited[len(splited) - 1]):
                return False

        return True
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import canBeCombined, isCss3PrefixProp, containsHack
from combiners.CombinerFactory import doCombine

class FEDCombineInToOne(RuleSetChecker):
    
    '''{
        "summary":"将多个子样式合并",
        "desc":"有的子样式可以合并为总样式，包括
            <code>margin</code> <code>padding</code> <code>font</code> <code>background</code> <code>border</code>
            等，合并以后可以获得更好的执行效率和压缩效果，<br/>
            例如：<br/>
            <code>.test {margin:4px; margin-right:0;}</code><br/>
            <code>==></code><br/>
            <code>.test{margin:4px 0 4px 4px}</code><br/>
        "
    }'''

    def __init__(self):
        self.id = 'combine-into-one'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_rough = 'should combine "%s" to "%s" in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        rules = ruleSet.getRules()

        counter = self._countCanBeCombined(rules)

        for name, value in counter.items():
            if name == 'font' and len(value) > 2 or name != 'font' and len(value) > 1:
                self.errorMsg = self.errorMsg_rough % (','.join(value), name)
                return False
        return True 

    def fix(self, ruleSet, config):
        rules = ruleSet.getRules()
        counter = self._countCanBeCombined(rules, True)
        rules = self._combineAttrs(rules, counter)
        ruleSet.setRules(rules)

    def _countCanBeCombined(self, rules, forFix = False):
        counter = {}
        for rule in rules:
            name = rule.name
            if rule.name != rule.strippedName:
                continue
            # do not do any hack combine
            if containsHack(rule):
                continue
            # -moz-border-radius, -o-border-radius is not for me
            if isCss3PrefixProp(name):
                continue

            bigger = canBeCombined(name)
            if bigger is not None:
                if counter.has_key(bigger):
                    if forFix:
                        counter[bigger].append([name, rule.fixedName, rule.fixedValue])
                    else:
                        counter[bigger].append(name)
                else:
                    if forFix:
                        counter[bigger] = [[name, rule.fixedName, rule.fixedValue]]
                    else:
                        counter[bigger] = [name]
        return counter

    def _combineAttrs(self, rules, counter):
        originRules = rules
        for name, value in counter.items():
            combined, deleted, hasFather = doCombine(name, value)
            if combined == None:
                continue

            newRules = []
            for rule in originRules:
                if containsHack(rule):
                    newRules.append(rule)
                    continue
                # it is what i want
                if rule.fixedName == name:
                    rule.fixedValue = combined
                    newRules.append(rule)
                    continue
                # it is what i want to delete
                if rule.fixedName in deleted:
                    if not hasFather:
                        rule.reset(name, combined)
                        newRules.append(rule)
                        hasFather = True
                    continue
                newRules.append(rule)
            originRules = newRules
        return originRules
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import hasHackChars
from ckstyle.browsers.BinaryRule import ALL
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

        # ".a {width:0} .a, .b{width:1}, .b{width:0}" should not be combined to ".a, .b{width:0} .a, .b{width:1}"
        for i in range(length):            
            if mapping[i][0] == 'extra':
                continue
            selectorHistory = []

            for j in range(i + 1, length):                
                if mapping[i][1] != mapping[j][1]:
                    selectorHistory.extend(splitedSelectors[j])
                    continue                    
                # bakcground-position is dangerous
                if mapping[j][1].find('background-position') != -1:
                    selectorHistory.extend(splitedSelectors[j])
                    continue

                hasFlag = False
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
            if r.extra or hasHackChars(r.selector) or r.selector.find('%') != -1:
                # make it impossible to equal
                mapping.append(['extra', "do_not_combine_" + str(counter)])
                counter = counter + 1
                continue
            mapping.append([r.selector, r.compressRules(browser)])
        return mapping
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDCommentLengthLessThan80(RuleSetChecker):

    '''{
        "summary":"注释不能超过80个字符",
        "desc":"注释长度不能超过80个字符，40个汉字，如果超出，则应该要换行~"
    }'''

    def __init__(self):
        self.id = 'comment-length'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg = 'comment for "${selector}" length should less than 80 per line'

    def check(self, ruleSet, config):
        comment = ruleSet.roughComment
        if len(comment) == 0:
            return True

        cs = comment.split('\n')
        for c in cs:
            if len(c.strip()) > 80:
                return False
        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isCss3Prop, isCss3PrefixProp, doNotNeedPrefixNow

class FEDCss3PropPrefix(RuleChecker):

    '''{
        "summary":"CSS3前缀相关检查",
        "desc":"CSS3属性的前缀，有的可以省略，比如：<br>
            <code>border-radius</code><br>
            有的是省略，必须写全，比如：<br><code>transition</code> <code>transform</code>等<br>
            在编写顺序上，本工具要求按照<br>
            <code>-webkit-,-moz-,-ms-,-o-,std</code><br>的顺序来编写，并且严格将属性的第一个字符对齐。"
    }'''

    def __init__(self):
        self.id = 'css3-with-prefix'
        self.errorLevel_keepInOrder = ERROR_LEVEL.WARNING
        self.errorLevel_missing = ERROR_LEVEL.ERROR
        self.errorLevel = ERROR_LEVEL.LOG

        self.errorMsg_keepInOrder = 'css3 prop "${name}" should keep in "-webkit-,-moz-,-ms-,-o-,std" order in "${selector}"'
        self.errorMsg_missing = 'css3 prop "${name}" missing some of "-webkit-,-moz-,-o-,std" in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        name = rule.name
        # only for css3 props
        if not isCss3Prop(name):
            return True

        if not isCss3PrefixProp(name):
            return True

        if doNotNeedPrefixNow(name):
            return True
        
        ruleSet = rule.getRuleSet()
        webkitName = '-webkit-' + name
        mozName = '-moz-' + name
        msName = '-ms-' + name # not necessary
        oName = '-o-' + name

        if not (ruleSet.existRoughNames(webkitName) 
                and ruleSet.existRoughNames(mozName)
                and ruleSet.existRoughNames(oName)
                and ruleSet.existRoughNames(name)):
            self.errorMsg = self.errorMsg_missing
            self.errorLevel = self.errorLevel_missing
            return False

        # in order -webkit-  -moz-  -ms-  -o-  std
        webkit = ruleSet.indexOf(webkitName)
        moz = ruleSet.indexOf(mozName)
        ms = ruleSet.indexOf(msName)
        if ms == -1:
            ms = moz
        o = ruleSet.indexOf(oName)
        std = ruleSet.indexOf(name)

        if not (webkit < moz <= ms < o < std):
            self.errorMsg = self.errorMsg_keepInOrder
            self.errorLevel = self.errorLevel_keepInOrder
            return False
        return True
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isCss3Prop, isCss3PrefixProp, doNotNeedPrefixNow
import re

pattern = re.compile('%\d+')
class FEDCss3PropSpaces(RuleChecker):
    
    '''{
        "summary":"CSS3缩进相关检查",
        "desc":"CSS3属性的缩进，必须将属性名称的第一个字符对齐。即：<br>
            <code>-webkit-transition:3s;</code>
            <br><code>&nbsp;&nbsp;&nbsp;-moz-transition:3s;</code>
            <br><code>&nbsp;&nbsp;&nbsp;&nbsp;-ms-transition:3s;</code>
            <br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-o-transition:3s;</code>
            <br><code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transition:3s;</code>
        "
    }'''

    def __init__(self):
        self.id = 'css3-prop-spaces'

        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_multi = 'css3 prop "${name}" should align to right in "${selector}"'
        self.errorMsg_single = 'should have 1(only) space before css3 prop "${name}" in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        name = rule.name
        # only for css3 props
        if not isCss3Prop(name):
            return True

        if not isCss3PrefixProp(name):
            return True
        
        if doNotNeedPrefixNow(name):
            # if exists prefix, then should keep spaces
            if not rule.getRuleSet().existRoughNames('-webkit-%s,-moz-%s,-ms-%s,-o-%s' % (name,name,name,name)):
                return True

        roughName = rule.roughName

        if rule.getRuleSet().singleLineFlag is False:
            # 12 = 4 + 8, 4 spaces, 8 for align
            if len(roughName.split(name)[0]) != 12:
                self.errorMsg = self.errorMsg_multi
                return False
        else:
            if roughName.startswith('  ') or not roughName.startswith(' '):
                self.errorMsg = self.errorMsg_single
                return False
        return True

    def fix(self, rule, config):
        name = rule.name
        # only for css3 props
        if not isCss3Prop(name):
            return

        if not isCss3PrefixProp(name):
            return

        if not rule.getRuleSet().existRoughNames('-webkit-%s,-moz-%s,-ms-%s,-o-%s' % (name,name,name,name)):
            return

        fixedName = rule.fixedName
        prefix = fixedName.split(name)[0]
        if rule.selector.find('%') != -1:
            remained = '-webkit-,-moz-,-ms-,-o-,'.replace(prefix + ',', '')
            testString = ','.join([(x + name) for x in remained[:-1].split(',')])
            if not rule.getRuleSet().existRoughNames(testString):
                return
        rule.fixedName = ((8 - len(prefix)) * ' ' if not config.fixToSingleLine else '') + fixedName
#/usr/bin/python
#encoding=utf-8

from Base import *
import string
from ckstyle.browsers.Detector import Browser

class FEDDistinguishBrowserExtra(ExtraChecker):
    
    '''{
        "summary":"嵌套规则区分浏览器",
        "desc":"目的是针对不同的浏览器，生成不同的CSS规则集"
    }'''

    def __init__(self):
        self.id = 'extra-for-browsers'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = ''

    def check(self, ruleSet, config):
        return True

    def fix(self, ruleSet, config):
        if not ruleSet.nested:
            return
        Browser.handleNestedStatement(ruleSet)#/usr/bin/python
#encoding=utf-8

from Base import *
import string
from ckstyle.browsers.Detector import Browser

class FEDDistinguishBrowserRule(RuleChecker):
    
    '''{
        "summary":"在属性级别区分浏览器",
        "desc":"目的是针对不同的浏览器，生成不同的CSS"
    }'''

    def __init__(self):
        self.id = 'rule-for-browsers'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = ''

    def check(self, rule, config):
        return True

    def fix(self, rule, config):
        Browser.handleRule(rule)#/usr/bin/python
#encoding=utf-8

from Base import *
import string
from ckstyle.browsers.Detector import Browser

class FEDDistinguishBrowserRuleSet(RuleSetChecker):
    
    '''{
        "summary":"在规则集级别区分浏览器",
        "desc":"目的是针对不同的浏览器，生成不同的CSS规则集"
    }'''

    def __init__(self):
        self.id = 'ruleset-for-browsers'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = ''

    def check(self, ruleSet, config):
        return True

    def fix(self, ruleSet, config):
        Browser.handleRuleSet(ruleSet)#/usr/bin/python
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
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isHTMLTag

class FEDDoNotSetStyleForTagOnly(RuleSetChecker):
    
    '''{
        "summary":"不要为html tag设置样式",
        "desc":"除了重置 CSS(如Reset.css) 的相关设置，其他代码一律不允许为html tag设置样式。"
    }'''

    def __init__(self):
        self.id = 'no-style-for-tag'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'should not set style for html tag in "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector.lower()
        if selector.find('@media') != -1:
            return True
        if selector.find('@-moz-document') != -1:
            return True
        selectors = selector.split(',')
        for s in selectors:
            if isHTMLTag(s.strip()):
                return False
        return True 
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
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDFixNestedStatement(ExtraChecker):
    
    '''{
        "summary":"修复嵌套的CSS",
        "desc":"@keyframes, @media之类的"
    }'''

    def __init__(self):
        self.id = 'fix-nested-ruleset'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = ''
        self.private = True

    def check(self, ruleSet, config):
        return True

    def fix(self, ruleSet, config):
        if not ruleSet.nested:
            return
        ruleSet.fixedSelector = ruleSet.fixedSelector.replace('"', '\'')
        statement = ruleSet.fixedStatement
        if (hasattr(config, 'operation') and getattr(config, 'operation') == 'compress'):
            from ckstyle.doCssCompress import prepare
            checker = prepare(statement, '', config)
            # 嵌套的CSS，如果是压缩，也需要精简
            msg = checker.doCompress(config._curBrowser)
            ruleSet.fixedStatement = msg
        else:
            from ckstyle.doCssFix import doFix
            checker, msg = doFix(statement, '', config)
            ruleSet.fixedStatement = msg
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDFixOutlineZero(RuleChecker):
    
    '''{
        "summary":"修复outline:none",
        "desc":"<code>outline:none</code> 和 <code>outline:0</code> 实现了相同的功能，但是后者的代码更简洁，便于压缩。"
    }'''

    def __init__(self):
        self.id = 'outline-zero'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = ''

    def check(self, rule, config):
        return True

    def fix(self, rule, config):
        if rule.name == 'outline' and rule.fixedValue == 'none':
            rule.fixedValue = '0'#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDFontSizeShouldBePtOrPx(RuleChecker):
    
    '''{
        "summary":"字体的单位必须用px或pt",
        "desc":"字体的单位可以有很多种，比如 <code>px pt em %</code> 等等，为了统一取值，统一要求为 <code>px/pt</code> ， 例如：<br>
            <code>font-size: 12px;</code><br>
            <code>font-size: 14pt;</code>"
    }'''

    def __init__(self):
        self.id = 'font-unit'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_ptOrPx = 'font-size unit should be px/pt in "${selector}"'
        self.errorMsg_xsmall = 'font-size should not be small/medium/large in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        if rule.name != 'font-size':
            return True

        value = rule.value
        if value.find('small') != -1 or value.find('medium') != -1 or value.find('large') != -1:
            self.errorMsg = self.errorMsg_xsmall
            return False

        if value == '0':
            return True

        if value.endswith('pt'):
            return True

        if value.endswith('px'):
            return True

        self.errorMsg = self.errorMsg_ptOrPx
        return False
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isCss3PrefixProp

class FEDHackAttributeInCorrectWay(RuleChecker):
    
    '''{
        "summary":"hack属性时的检查",
        "desc":"必须使用正确的 hack 方式， 比如 <code>_ * +</code> 等，其他的属性前缀一律不允许"
    }'''

    def __init__(self):
        self.id = 'hack-prop'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = '"${name}" is not in correct hacking way in "${selector}"'

    def check(self, rule, config):
        if rule.value.find(r'\0') != -1:
            return False

        stripped = rule.roughName.strip()
        if rule.name == stripped.lower():
            return True

        if isCss3PrefixProp(rule.name):
            return True

        if not stripped.startswith('_') and not stripped.startswith('*') and not stripped.startswith('+'):
            return False

        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDHackRuleSetInCorrectWay(ExtraChecker):
    
    '''{
        "summary":"hack规则时的检查",
        "desc":"针对Firefox Opera Safari等浏览器的 hack 方式， <strong>人人FED CSS编码规范</strong>中有详细的描述， 
            不允许使用规定之外的方式进行规则级别的hack"
    }'''

    def __init__(self):
        self.id = 'hack-ruleset'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'not correct hacking way in "${selector}"'

    def check(self, ruleSet, config):
        if not ruleSet.nested:
            return True

        selector = ruleSet.selector.strip()
        if selector.find('@-moz-document') != -1:
            if selector != '@-moz-document url-prefix()':
                return False

        if selector.find('-webkit-min-device-pixel-ratio:0') != -1:
            if selector != '@media screen and (-webkit-min-device-pixel-ratio:0)' and selector.find('-webkit-min-device-pixel-ratio:10000') == -1:
                return False

        if selector.find('-webkit-min-device-pixel-ratio:10000') != -1:
            if selector.find('@media all') == -1 or selector.find('not all and') == -1 or selector.find('-webkit-min-device-pixel-ratio:0') == -1:
                return False

        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *
import re

pattern_color = re.compile(r'#([a-f0-9A-F]+)')

class FEDHexColorShouldUpper(RuleChecker):
    '''{
        "summary":"16进制颜色大写&缩写",
        "desc":"<p>浏览器会先将小写的颜色值转换成大写，所以写成大写格式可以省略这部分的开销，并且尽量省略，例如：
            </br><code>color:#ffffff; </code><br/><code>==></code><br/><code>color:#FFF;</code></p>"
    }'''

    def __init__(self):
        self.id = 'hexadecimal-color'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_length = 'wrong color length(should be 3 or 6) in "${selector}"'
        self.errorMsg_replace = 'replace "#%s" with "#%s" in "${selector}"'
        self.errorMsg_upper = 'color should in upper case in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        value = rule.value
        if value.find('#') == -1:
            return True

        found = self._findColor(rule.value)
        for f in found:
            flag = self._checkEach(f)
            if not flag:
                return False
        return True

    def _checkEach(self, found):
        if found is None:
            return True

        if self._isLower(found):
            self.errorMsg = self.errorMsg_upper
            return False

        if len(found) == 3:
            return True

        if self._wrongLength(found):
            self.errorMsg = self.errorMsg_length
            return False

        if self._isDuplicate(found):
            self.errorMsg = self.errorMsg_replace % (found, found[0]+found[2]+found[4])
            return False
        
        return True

    def fix(self, rule, config):
        value = rule.fixedValue
        if value.find('#') == -1:
            return

        hasImportant = rule.fixedValue.find('important') != -1
        found = self._findColor(rule.fixedValue)
        for f in found:
            self._fixEach(rule, f, hasImportant)

    def _fixEach(self, rule, found, hasImportant):
        if self._isLower(found):
            rule.fixedValue = rule.fixedValue.replace('#' + found, '#' + found.upper())
            found = found.upper()

        if len(found) == 3:
            return

        if not hasImportant and self._wrongLength(found):
            final = found[0:6] if len(found) > 6 else (found + (6 - len(found)) * 'F')
            rule.fixedValue = rule.fixedValue.replace('#' + found, '#' + final)
            found = final

        if self._isDuplicate(found):
            rule.fixedValue = rule.fixedValue.replace('#' + found, '#' + found[0] + found[2] + found[4])

    def _wrongLength(self, found):
        return len(found) != 3 and len(found) != 6

    def _isLower(self, found):
        return found is not None and found != found.upper()

    def _isDuplicate(self, found):
        return found[0] == found[1] and found[2] == found[3] and found[4] == found[5]

    def _findColor(self, value):
        splited = value.split(' ')
        found = []
        for x in splited:
            x = x.strip()
            matcher = pattern_color.findall(x)
            if matcher is not None:
                found.extend(matcher)
            #if x.startswith('#'):
            #    found.append(x.split('!important')[0][1:].split(',')[0].split(')')[0])
            #elif x.find('(#') != -1:
            #    found.append(x.split('(#')[1].split('!important')[0].split(',')[0].split(')')[0])
        return found
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isHTMLTag

class FEDHighPerformanceSelector(RuleSetChecker):
    
    '''{
        "summary":"针对低性能的选择器的检查",
        "desc":"低性能选择器，害人害己还集体，本工具收集了一些低性能选择器的情形，具体请参见：<br>
            <code>FEDHighPerformanceSelector.py</code>中的相关内容"
    }'''

    def __init__(self):
        self.id = 'high-perf-selector'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_shorter = 'please shorter the selector "${selector}"'
        self.errorMsg_no1 = 'do not use low performance selector ">" in "${selector}"'
        self.errorMsg_lessTag = 'use less tag in "${selector}"'
        self.errorMsg_id = 'should not put "HTMLtag" and "#id" together in "${selector}"'
        self.errorMsg_class = 'should not put "HTMLtag" and ".class" together in "${selector}"'
        self.errorMsg_reg = 'should not use ~=,^=,|=,$=,*= in selector of "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        selectors = ruleSet.selector.replace('  ', '').split(',')
        for s in selectors:
            if s.find('@media') != -1:
                continue

            if s.find('=') != -1:
                if s.find('~=') != -1 or s.find('^=') != -1 or s.find('|=') != -1 or s.find('$=') != -1 or s.find('*=') != -1:
                    self.errorMsg = self.errorMsg_reg
                    return False

            splited = s.split(' ')
            if len(splited) > 5:
                self.errorMsg = self.errorMsg_shorter
                return False
            counter = 0
            for p in splited:
                if p == '>':
                    self.errorMsg = self.errorMsg_no1
                    return False

                innerSplit = p.split('#')
                if len(innerSplit) == 2 and isHTMLTag(innerSplit[0]):
                    self.errorMsg = self.errorMsg_id
                    return False

                innerSplit = p.split('.')
                if len(innerSplit) == 2 and isHTMLTag(innerSplit[0]):
                    self.errorMsg = self.errorMsg_class
                    return False

                if isHTMLTag(p):
                    counter = counter + 1
            if counter > 1:
                self.errorMsg = self.errorMsg_lessTag
                return False

        noSpace = ruleSet.selector.replace(' ', '')
        if noSpace.find('ulli') != -1 or noSpace.find('olli') != -1 or noSpace.find('dldt') != -1 or noSpace.find('dldd') != -1:
            self.errorMsg = self.errorMsg_lessTag
            return False
        return True
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDMultiLineBraces(RuleSetChecker):
    
    '''{
        "summary":"多行CSS风格的括号检查",
        "desc":"用于检查多行风格下的 <code>{</code> 和 <code>}</code> 的编写风格，前后空格符和回车符的情况等。"
    }'''

    def __init__(self):
        self.id = 'multi-line-brace'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_shouldEnterAfterOpenningBrace = 'should "enter" after the opening brace in "${selector}"'
        self.errorMsg_shouldEnterBeforeClosingBrace = 'should "enter" before the closing brace in "${selector}"'
        self.errorMsg_extraSpaceAfterOpeningBrace = 'extra "space" after the opening brace in "${selector}"'
        self.errorMsg_everyAttrShouldInSingleLine = 'every name/value should in single line in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        singleLine = ruleSet.getSingleLineFlag()
        if singleLine:
            return True

        value = ruleSet.roughValue
        splited = value.split('\n')
        if splited[0].strip() != '':
            self.errorMsg = self.errorMsg_shouldEnterAfterOpenningBrace
            return False

        if splited[0].strip() == '' and splited[0].startswith(' '):
            self.errorMsg = self.errorMsg_extraSpaceAfterOpeningBrace
            return False

        ruleLength = len(ruleSet.getRules())
        if ruleLength != 0 and len(value.strip().split('\n')) != ruleLength:
            self.errorMsg = self.errorMsg_everyAttrShouldInSingleLine
            return False

        if not value.replace(' ', '').endswith('\n'):
            self.errorMsg = self.errorMsg_shouldEnterBeforeClosingBrace
            return False

        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDMultiLineSelectors(RuleSetChecker):
    
    '''{
        "summary":"多行CSS风格的选择器检查",
        "desc":"多行风格下，每一个选择器单独占一行，并以逗号结尾，例如：<br>
            <code>.a,</code><br>
            <code>.b,</code><br>
            <code>.c {</code><br>
            <code>&nbsp;&nbsp;&nbsp;&nbsp;width: 100px;</code><br>
            <code>}</code>
        "
    }'''

    def __init__(self):
        self.id = 'multi-line-selector'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_multiSelectorBeforeSemicolon = 'should not have "space" before semicolon in "${selector}"'
        self.errorMsg_multiSelectorBeforeSemicolon = 'should not have "space" after semicolon in "${selector}"'
        self.errorMsg_shouldEnter = 'should enter in multi-selector, in "${selector}"'
        self.errorMsg_tooManyEnters = 'too many "enter"s in "${selector}"'
        self.errorMsg_startsWithSpace = 'selector should not start with "space" in "${selector}"'
        self.errorMsg_extraSpaceAfterComma = 'extra "space" after comma in "${selector}"'
        self.errorMsg_extraSpaceBeforeComma = 'extra "space" before comma in "${selector}"'
        self.errorMsg_commaInTheEnd = 'comma should at the end of selector in "${selector}"'
        self.errorMsg_shouldAddSpaceForLast = 'should add "space" for last selector of "${selector}"'
        self.errorMsg_shouldNotEnterAtTheEnd = 'should not "enter" at the end of "${selector}"'
        self.errorMsg_selectorEndsWithSpace = 'selector should end with only one space "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        selector = ruleSet.roughSelector

        if not selector.endswith(' ') or selector.endswith('  '):
            self.errorMsg = self.errorMsg_selectorEndsWithSpace
            return False

        if selector.find(',') == -1:
            return True

        if selector.replace(' ', '').endswith('\n'):
            self.errorMsg = self.errorMsg_shouldNotEnterAtTheEnd
            return False

        if selector.strip().find('\n') == -1:
            self.errorMsg = self.errorMsg_shouldEnter
            return False

        selectors = selector.split('\n')
        length = len(selectors)

        if len(selector.split(',')) != len(selector.strip().split('\n')):
            self.errorMsg = self.errorMsg_tooManyEnters
            return False

        realSelectors = []
        for s in selectors:
            if s.strip() != '':
                realSelectors.append(s)

        counter = 0
        length = len(realSelectors)
        for current in realSelectors:
            counter = counter + 1
            stripped = current.strip()
            if stripped == '':
                continue
            if current.startswith(' '):
                self.errorMsg = self.errorMsg_startsWithSpace
                return False
            if stripped.endswith(' ,'):
                self.errorMsg = self.errorMsg_extraSpaceBeforeComma
                return False
            if current.endswith(' ') and stripped.endswith(','):
                self.errorMsg = self.errorMsg_extraSpaceAfterComma
                return False
            if counter == length and not current.endswith(' '):
                self.errorMsg = self.errorMsg_shouldAddSpaceForLast
                return False
            if counter != length and stripped.find(',') == -1:
                self.errorMsg = self.errorMsg_commaInTheEnd
                return False

        return True 

        
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isCss3PrefixProp

class FEDMultiLineSpaces(RuleChecker):
    
    '''{
        "summary":"CSS多行风格的空格检查",
        "desc":"多行风格下，CSS的空格检查包括：
            <ol>
                <li>选择器的空格</li>
                <li>属性的空格</li>
                <li>结尾}的空格</li>
            </ol>
            具体请参见人人相关的CSS规范"
    }'''

    def __init__(self):
        self.id = 'multi-line-space'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_name_pre = 'should have 4 spaces before "${name}" in "${selector}"'
        self.errorMsg_name_after = 'should not have "space" after "${name}" in "${selector}"'
        self.errorMsg_value_pre = 'should have (only) one "space" before value of "${name}" in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        singleLine = rule.getRuleSet().getSingleLineFlag()
        if singleLine:
            return True
        
        prefix = ' ' * 4
        name = rule.roughName
        value = rule.roughValue
        stripped = rule.roughName.strip()

        # leave special css3 props for FEDCss3AttrChecker
        if isCss3PrefixProp(rule.name):
            if name.endswith(' '):
                self.errorMsg = self.errorMsg_name_after
                return False

            if not value.startswith(' ') or value.startswith('  '):
                self.errorMsg = self.errorMsg_value_pre
                return False

            return True

        if name.find('\t') != -1:
            name = name.replace('\t', prefix)
        if not name.startswith(prefix):
            self.errorMsg = self.errorMsg_name_pre
            return False
        if name.startswith(' ' * 5):
            self.errorMsg = self.errorMsg_name_pre
            return False
        if name.endswith(' '):
            self.errorMsg = self.errorMsg_name_after
            return False

        if not value.startswith(' ') or value.startswith('  '):
            self.errorMsg = self.errorMsg_value_pre
            return False

        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isHTMLTag

class FEDMustContainAuthorInfo(StyleSheetChecker):
    
    '''{
        "summary":"需要在文件中添加作者信息",
        "desc":"需要在文件中添加作者的信息，本工具认可的作者信息是在文件顶部的注释中添加 <code>@author:xxx</code>"
    }'''

    def __init__(self):
        self.id = 'add-author'
        self.errorMsg_author = 'should add @author in the head of "${file}"'
        self.errorMsg_empty = 'empty css file "${file}"'
        self.errorMsg = ''
        self.errorLevel = ERROR_LEVEL.ERROR

    def check(self, styleSheet, config):
        ruleSets = styleSheet.getRuleSets()
        if len(ruleSets) == 0:
            self.errorMsg = self.errorMsg_empty
            return False

        first = ruleSets[0]

        if styleSheet.getFile() != '' and first.comment.find('@author') == -1 and first.comment.find('@renren-inc.com') == -1:
            self.errorMsg = self.errorMsg_author
            return False
        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDNoAlphaImageLoader(RuleChecker):
    
    '''{
        "summary":"不要使用AlphaImageLoader",
        "desc":"<code>AlphaImageLoader</code> 主要用于在IE6下显示半透明图片，此举实际上费力不讨好，
            对IE的性能影响极大，为了更好地实现网页的 <strong>渐进增强</strong> 
            ，建议不要使用 <code>AlphaImageLoader</code>"
    }'''

    def __init__(self):
        self.id = 'no-alpha-image-loader'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'should not use AlphaImageLoader in "${selector}"'

    def check(self, rule, config):
        if rule.value.find('AlphaImageLoader') != -1:
            return False
        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import existsAppearanceWords

class FEDNoAppearanceNameInSelector(RuleSetChecker):
    
    '''{
        "summary":"选择器中避免表现相关的词汇",
        "desc":"避免将在selector中出现 <code>.red</code> <code>.left</code> 等描述性词汇，
            用具体的实际意义来代替，比如 <code>.error</code> <code>.sidebar</code> "
    }'''

    def __init__(self):
        self.id = 'no-appearance-word-in-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_origin = 'should not use appearance word "%s" in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        selector = ruleSet.selector.lower()

        if selector.find('@media') != -1:
            return True
        if selector.find('@-moz-document') != -1:
            return True

        word = existsAppearanceWords(selector)
        if word is not None:
            self.errorMsg = self.errorMsg_origin % word
            return False

        return True
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
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDNoEmptyRuleSet(RuleSetChecker):
    
    '''{
        "summary":"删除空的规则",
        "desc":"空的CSS规则集是没有任何意义的，应该直接删除掉"
    }'''

    def __init__(self):
        self.id = 'no-empty-ruleset'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'empty ruleset found "${selector}"'

    def check(self, ruleSet, config):
        if len(ruleSet.getRules()) == 0:
            return False
        return True 

    def fix(self, ruleSet, config):
        if len(ruleSet.getRules()) == 0:
            styleSheet = ruleSet.getStyleSheet()
            styleSheet.removeRuleSet(ruleSet)
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
#/usr/bin/python
#encoding=utf-8

from Base import *
import re
pattern_number = re.compile('\d+')

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
            
        found = pattern_number.findall(selector)
        for x in found:
            if selector.find('v' + x) == -1 and selector.find('step' + x) == -1  and selector.find('item' + x) == -1 and selector.find('h' + x) == -1 :
                return False
        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDNoStarInSelector(RuleSetChecker):
    
    '''{
        "summary":"不要在选择器中使用星号",
        "desc":"禁止在选择器中加入<code>*</code>来选择所有元素，例如：<br>
            <br>
            <code>*html</code> <code>*+html</code> <code>*:not</code>等几种特殊hack除外"
    }'''

    def __init__(self):
        self.id = 'no-star-in-selector'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'please remove low performance selector "*" from "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector
        if selector.find('*') == -1:
            return True

        replaced = selector.replace(' ', '')
        if replaced.startswith('*html') or replaced.startswith('*+html'):
            return True

        if replaced.find('*:not') != -1:
            return True

        # give it to FEDHighPerformanceSelector.py
        if replaced.find('*=') != -1 and len(replaced.split('*')) == 2:
            return True

        return False
#/usr/bin/python
#encoding=utf-8

from Base import *
import re

pattern_unit = re.compile(r'(0\s*[\w]+)')
replacer_unit = re.compile(',\s+')

class FEDNoUnitAfterZero(RuleChecker):
    
    '''{
        "summary":"删除0后面的单位",
        "desc":"0后面的单位可以删除，以实现更好的压缩。比如 <code>0px ==> 0</code> ，<code>0em ==> 0</code> 等，
            但是<code>transition: 0s</code>的<code>s</code>不能省略"
    }'''

    def __init__(self):
        self.id = 'del-unit-after-zero'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'unit should be removed when meet 0 in "${selector}"'

    def check(self, rule, config):

        values = rule.value.split(' ')

        for v in values:
            v = v.strip()
            if v.find('(') != -1:
                matched = self._startsWithZero(v.split('(')[1])
            else:
                matched = self._startsWithZero(v)

            if matched is None:
                continue

            for m in matched:
                if m != '0s':
                    return False

        return True 

    def fix(self, rule, config):
        if rule.name == 'expression':
            return

        fixed = rule.fixedValue
        rule.fixedValue = rule.fixedValue.replace(',', ', ')

        collector = []
        for v in rule.fixedValue.split(' '):
            v = v.strip()
            if v.find('(') != -1:
                matched = self._startsWithZero(v.split('(')[1])
            else:
                matched = self._startsWithZero(v)

            if matched is None:
                collector.append(v)
                continue

            finalV = v;
            for m in matched:
                if m != '0s':
                    finalV = finalV.replace(m, '0')
            collector.append(finalV)

        rule.fixedValue = replacer_unit.sub(', ', ' '.join(collector))

    def _startsWithZero(self, value):
        matcher = pattern_unit.match(value)
        if matcher is not None:
            return matcher.groups()
        return None
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDNoZeroBeforeDot(RuleChecker):
    
    '''{
        "summary":"删除0.x前面的0",
        "desc":" 0.xxx 前面的 0 是可以删除的，以实现更好的压缩。例如<br>
            <code>0.3px ==> .3px</code><br><br>
            <code>rgba(0,0,0,0.3)<code><br>
            <code>==></code><br>
            <code>rgba(0,0,0,.3)</code>"
    }'''

    def __init__(self):
        self.id = 'no-zero-before-dot'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'zero should be removed when meet 0.xxx in "${selector}"'

    def check(self, rule, config):
        value = rule.value

        if self._startsWithZeroDot(value):
            return False

        values = rule.value.split(' ')
        for v in values:
            if self._startsWithZeroDot(v.strip()):
                return False

        return True 

    def fix(self, rule, config):
        fixedValue = rule.fixedValue
        for v in fixedValue.split(' '):
            if self._startsWithZeroDot(v):
                rule.fixedValue = rule.fixedValue.replace(v, v[1:])

    def _startsWithZeroDot(self, value):
        return value.startswith('0.')
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDRemoveDuplicatedAttr(RuleSetChecker):
    
    '''{
        "summary":"删除重复的属性设置",
        "desc":"如果在一个规则集中，对相同的两个属性进行了赋值，而且取值相同，则可以删除前面的赋值，例如：
            <br>
            <code>.test {</code><br>
            <code>&nbsp;&nbsp;&nbsp;&nbsp;width: 100px;</code><br>
            <code>&nbsp;&nbsp;&nbsp;&nbsp;width: 100px;</code><br>
            <code>}</code><br>
            <code>==></code><br>
            <code>.test {</code><br>
            <code>&nbsp;&nbsp;&nbsp;&nbsp;width: 100px;</code><br>
            <code>}</code>"
    }'''

    def __init__(self):
        self.id = 'remove-duplicated-attr'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'has more than 1 ${name} in "${selector}"'

    def check(self, ruleSet, config):
        rules = ruleSet.getRules()
        collector = []
        for rule in rules:
            info = self.ruleInfo(rule)
            if info in collector:
                return False
            collector.append(info)
        return True

    def fix(self, ruleSet, config):
        # make sure we use the last statement, so reverse and filter and reverse again
        # [a1, a2, b, c] ==> [c, b, a2, a1] ==> [c, b, a2] ==> [a2, b, c]
        rules = ruleSet.getRules()
        rules.reverse()
        newRules = []
        collector = []
        for rule in rules:
            info = self.ruleInfo(rule)
            if not info in collector:
                collector.append(info)
                newRules.append(rule)
        newRules.reverse()
        ruleSet.setRules(newRules)

    def ruleInfo(self, rule):
        if rule.fixedName != '':
            return rule.fixedName + ':' + rule.fixedValue
        return rule.strippedName + ':' + rule.strippedValue
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDReplaceBorderZeroWithBorderNone(RuleChecker):
    
    '''{
        "summary":"用border:none替换border:0",
        "desc":"<code>border:0</code> 实际上是有border的，只不过宽度为0， 而 <code>border:none;</code> 
            是根本没有border的，对于浏览器来说后者的效率高，但是要注意，后者的代码长度稍微长一些。"
    }'''

    def __init__(self):
        self.id = 'no-border-zero'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_borderWidth = 'replace "border-width: 0" with "border-width: none" in "${selector}"'
        self.errorMsg_border = 'replace "border: 0" with "border: none" in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        if rule.name == 'border' and rule.value == '0':
            self.errorMsg = self.errorMsg_border
            return False

        if rule.name == 'border-width' and rule.value == '0':
            self.errorMsg = self.errorMsg_borderWidth
            return False

        return True
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDSelectorNoUnderLine(RuleSetChecker):
    
    '''{
        "summary":"不要在选择器中使用下划线",
        "desc":"在selector中不要使用下划线 <code>_</code> ，可以使用中划线 <code>-</code>"
    }'''

    def __init__(self):
        self.id = 'no-underline-in-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'should not use _ in selector "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector
        if selector.find('_') != -1:
            return False
        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDSemicolonAfterValue(RuleChecker):
    
    '''{
        "summary":"为每一个属性后添加分号",
        "desc":"按照CSS编码规范，每一个规则后面都必须加上分号 <code>;</code>"
    }'''

    def __init__(self):
        self.id = 'add-semicolon'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'each rule in "${selector}" need semicolon in the end, "${name}" has not'

    def check(self, rule, config):
        if not rule.roughValue.strip().endswith(';'):
            return False
        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDShouldNotUseImportant(RuleChecker):
    
    '''{
        "summary":"不要使用!important",
        "desc":"CSS中不要使用<code>!important</code>"
    }'''

    def __init__(self):
        self.id = 'do-not-use-important'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'Should not use !important in "${name}" of "${selector}"'

    def check(self, rule, config):
        value = rule.value
        if value.replace(' ', '').find('!important') != -1:
            return False
        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDSingleLineBraces(RuleSetChecker):
    
    '''{
        "summary":"单行的括号检查",
        "desc":"与单行CSS编码风格相关的括号检查"
    }'''

    def __init__(self):
        self.id = 'single-line-brace'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_openingBrace = 'should have "only one space" before the opening brace in "${selector}"'
        self.errorMsg_openingBraceEnd = 'should have "only one space" after the opening brace in "${selector}"'
        self.errorMsg_closingBrace = 'should have "only one space" before the closing brace in "${selector}"'
        self.errorMsg_closingBraceEnd = 'should have "only one space" before the closing brace in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        singleLine = ruleSet.getSingleLineFlag()
        if not singleLine:
            return True
        selector = ruleSet.roughSelector
        if selector.find(',') == -1:
            if selector.endswith('  ') or not selector.endswith(' '):
                self.errorMsg = self.errorMsg_openingBrace
                return False
        else:
            return True

        value = ruleSet.roughValue
        if not value.startswith(' ') or value.startswith('  '):
            self.errorMsg = self.errorMsg_openingBraceEnd
            return False
        if not value.endswith(' ') or value.endswith('  '):
            self.errorMsg = self.errorMsg_closingBraceEnd
            return False
        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDSingleLineSelector(RuleSetChecker):
    
    '''{
        "summary":"单行的选择器检查",
        "desc":"单行的选择器检查内容，请参考多行选择器检查和人人FED CSS编码规范"
    }'''

    def __init__(self):
        self.id = 'single-line-selector'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_noEnterInSingleSelector = 'should not "enter" at the end of "${selector}"'
        self.errorMsg_multiSelectorBeforeSemicolon = 'should not have "space" after semicolon in "${selector}"'
        self.errorMsg_shouldNotStartsWithSpace = 'should start with "space" in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        selector = ruleSet.roughSelector
        if selector.find(',') != -1:
            return True

        if selector.lstrip().find('\n') != -1:
            self.errorMsg = self.errorMsg_noEnterInSingleSelector
            return False

        splited = selector.split('\n')
        realSelector = splited[len(splited) - 1]
        
        if realSelector.startswith(' '):
            self.errorMsg = self.errorMsg_shouldNotStartsWithSpace
            return False

        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDSingleLineSpaces(RuleChecker):
    
    '''{
        "summary":"单行的空格检查",
        "desc":"单行CSS编码风格相关的空格检查，具体内容请参见CSS编码规范"
    }'''

    def __init__(self):
        self.id = 'single-line-space'
        self.errorLevel = ERROR_LEVEL.LOG
        self.errorMsg_noSpace = 'should have one "space" before "${name}" in "${selector}"'
        self.errorMsg_spaceEnd = 'should not have "space" after "${name}" in "${selector}"'
        self.errorMsg_noSpaceBeforeValue = 'should have one "space" before value of "${name}" in "${selector}"'
        self.errorMsg_extraSpaceAfterValue = 'found extra "space" after value of "${name}" in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        singleLine = rule.getRuleSet().getSingleLineFlag()
        if not singleLine:
            return True

        if not rule.roughName.startswith(' '):
            self.errorMsg = self.errorMsg_noSpace
            return False

        if rule.roughName.endswith(' '):
            self.errorMsg = self.errorMsg_spaceEnd
            return False
        
        if not rule.roughValue.startswith(' '):
            self.errorMsg = self.errorMsg_noSpaceBeforeValue
            return False

        value = rule.roughValue.strip()
        if value.endswith(' ;') or value.endswith(' '):
            self.errorMsg = self.errorMsg_extraSpaceAfterValue
            return False

        return True 
#/usr/bin/python
#encoding=utf-8

from helper import getAttrOrder
from Base import *

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
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import containsChnChar

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
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isCssProp

class FEDUnknownCssNameChecker(RuleChecker):
    
    '''{
        "summary":"错误的css属性",
        "desc":"本工具会帮您查找错误的CSS属性，如果写错了，即可收到错误提示"
    }'''

    def __init__(self):
        self.id = 'unknown-css-prop'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'unknown attribute name "${name}" found in "${selector}"'

    def check(self, rule, config):
        return isCssProp(rule.name.lower())
#/usr/bin/python
#encoding=utf-8

from Base import *
from helper import isHTMLTag

class FEDUnknownHTMLTagName(RuleSetChecker):
    
    '''{
        "summary":"错误的HTML Tag",
        "desc":"如果您输入了错误的HTML Tag，本工具也会给出响应的提示"
    }'''

    def __init__(self):
        self.id = 'unknown-html-tag'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_rough = 'unknown html tag "%s" found in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        selector = ruleSet.selector.lower()
        if selector.find('@media') != -1:
            return True
        if selector.find('@-moz-document') != -1:
            return True
        selectors = selector.split(',')
        for s in selectors:
            for r in s.split(' '):
                r = r.strip()
                if r != '':
                    if r.find('::') != -1:
                        # p::selection
                        tag = r.split('::')[0].split('.')[0].split('#')[0].strip()
                    else:
                        # abcd:hover
                        # abcd.class-name:hover
                        # abcd#class-name:hover
                        tag = r.split(':')[0].split('.')[0].split('#')[0].strip()

                    # .test > .inner
                    if tag == '' or tag == '>' or tag == '*' or tag == '+':
                        continue

                    # #id
                    if tag.find('#') != -1:
                        continue

                    # input[type=button]
                    if tag.find('[') != -1:
                        tag = tag.split('[')[0].strip()

                    # *+html
                    if tag.startswith('*+'):
                        tag = tag[2:]

                    # *html
                    elif tag.startswith('*'):
                        tag = tag[1:]

                    if not isHTMLTag(tag):
                        self.errorMsg = self.errorMsg_rough % tag
                        return False
        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDUseLowerCaseProp(RuleChecker):
    
    '''{
        "summary":"属性名称应该用小写",
        "desc":"所有的CSS属性名称一律小写，例如 <code>width</code> ，大写的方式是不正确的，
            例如： <code>WIDTH:100px;</code>"
    }'''

    def __init__(self):
        self.id = 'lowercase-prop'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_name = '"${name}" should use lower case, in "${selector}"'
        self.errorMsg_value = 'value of "${name}" should use lower case, in "${selector}"'
        self.errorMsg = ''

    def check(self, rule, config):
        value = rule.value
        name = rule.strippedName

        # give it to FED16ColorShouldUpper.py
        if name == 'color':
            return True

        if value.find('expression') != -1:
            return True

        if name.lower() != name:
            self.errorMsg = self.errorMsg_name
            return False

        if value.find('#') != -1:
            return True

        if name != 'font' and name != 'font-family' and value != value.lower() and value.find('#') == -1:
            self.errorMsg = self.errorMsg_value
            return False

        if name == 'font-family':
            return True

        if name == 'font':
            if value.find(',') != -1:
                # font: italic bold 12px/30px 'Courier New', Georgia, serif;
                other = ' '.join(value.split(',')[0].split("'")[0].split(' ')[0:-1])
                if other != other.lower():
                    self.errorMsg = self.errorMsg_value
                    return False
            return True

        if value.lower() != value:
            self.errorMsg = self.errorMsg_value
            return False

        return True 
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDUseLowerCaseSelector(RuleSetChecker):
    
    '''{
        "summary":"选择器用小写字母",
        "desc":"选择器应该用小写字母， 例如 <code>.demo</code> ， 不允许使用大写，例如： <code>.Demo .Test</code>"
    }'''

    def __init__(self):
        self.id = 'lowercase-selector'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'selector should use lower case, in "${selector}"'

    def check(self, ruleSet, config):
        selector = ruleSet.selector
        if selector.lower() != selector:
            return False

        return True 

    def fix(self, ruleSet, config):
        # if fix upper to lower, will cause error in HTML(do not do evil)
        pass
        #selector = ruleSet.selector
        #if selector.lower() != selector:
        #    ruleSet.fixedSelector = ruleSet.fixedSelector.lower()
#/usr/bin/python
#encoding=utf-8

from Base import *

class FEDUseSingleQuotation(RuleChecker):
    
    '''{
        "summary":"使用单引号",
        "desc":"CSS的属性取值一律使用单引号<code>'</code>， 不允许使用双引号"
    }'''

    def __init__(self):
        self.id = 'single-quotation'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg = 'replace " with \' in "${selector}"'

    def check(self, rule, config):
        if self._findDouble(rule.value):
            return False

        return True

    def fix(self, rule, config):
        if self._findDouble(rule.value):
            rule.fixedValue = rule.value.replace('"', "'")

    def _findDouble(self, value):
        return value.find('"') != -1
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
#/usr/bin/python
#encoding=utf-8

from Base import *
import string
from helper import isCss3PrefixProp

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
