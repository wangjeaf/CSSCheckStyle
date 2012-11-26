from Base import *

class FEDHackRuleSetInCorrectWay(RuleSetChecker):
    def __init__(self):
        self.id = 'hack-ruleset'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg = 'not correct hacking way in "${selector}"'

    def check(self, ruleSet, config):
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
