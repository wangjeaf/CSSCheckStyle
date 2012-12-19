from Base import *
from helper import isCss3Prop, isCss3PrefixProp, doNotNeedPrefixNow

class FEDCss3PropPrefix(RuleChecker):
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
