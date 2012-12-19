from Base import *
from helper import hasHackChars

class FEDCombineSameRuleSets(StyleSheetChecker):
    def __init__(self):
        self.id = 'combine-same-rulesets'
        self.errorMsg_empty = '"%s" and "%s" contains same rules, should be combined in ${file}"'
        self.errorMsg = ''
        self.errorLevel = ERROR_LEVEL.ERROR

    # can be checked correctly only after reorder/fix/compress, so do not check
    def check(self, styleSheet, config):
        return True 

    def fix(self, styleSheet, config):
        ruleSets = styleSheet.getRuleSets()
        mapping = self._gen_hash(ruleSets)

        length = len(mapping)
        # .a {width:0} .a, .b{width:1}, .b{width:0}
        
        
        for i in range(length):            
            if mapping[i][0] == 'extra':
                continue
            selectorHistory = []

            for j in range(i + 1, length):                
                if mapping[i][1] != mapping[j][1]:
                    selectorHistory.extend([x.strip() for x in mapping[j][0].split(',') if x.strip() is not ''])
                    continue
                hasFlag = False
                for x in mapping[j][0].split(','):
                    x = x.strip()
                    if x in selectorHistory:
                        hasFlag = True
                        break
                if hasFlag:
                    selectorHistory.extend([x.strip() for x in mapping[j][0].split(',') if x.strip() is not ''])
                    continue

                # make it different
                mapping[j][1] = str(i) + str(j)

                # extend target selector
                target = styleSheet.getRuleSets()[i]
                src = styleSheet.getRuleSets()[j]
                target.extendSelector(src)
                # remove rule set
                styleSheet.removeRuleSetByIndex(j)
                selectorHistory.extend([x.strip() for x in mapping[j][0].split(',') if x.strip() is not ''])

        # remember to clean after remove ruleset
        styleSheet.clean()

    def _gen_hash(self, ruleSets):
        mapping = []
        counter = 0
        for r in ruleSets:
            if r.extra or hasHackChars(r.selector):
                # make it impossible to equal
                mapping.append(['extra', "do_not_combine_" + str(counter)])
                counter = counter + 1
                continue
            mapping.append([r.selector, r.compressRules()])
        return mapping
