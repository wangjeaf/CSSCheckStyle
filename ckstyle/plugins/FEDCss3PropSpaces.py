from Base import *
from helper import isCss3Prop, isCss3PrefixProp, doNotNeedPrefixNow
import re

pattern = re.compile('%\d+')
class FEDCss3PropSpaces(RuleChecker):
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
