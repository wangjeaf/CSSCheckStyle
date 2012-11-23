from Base import *

class FEDCombineSameRuleSets(StyleSheetChecker):
    def __init__(self):
        self.id = 'combine-same-rulesets'
        self.errorMsg_empty = '"%s" and "%s" contains same rules, should be combined in ${file}"'
        self.errorMsg = ''
        self.errorLevel = ERROR_LEVEL.ERROR

    # can be checked correctly only after reorder/fix/compress, so do not check
    def check(self, styleSheet):
        return True 

    def fix(self, styleSheet):
        ruleSets = styleSheet.getRuleSets()
        mapping = self._gen_hash(ruleSets)

        length = len(mapping)

        for i in range(length):
            for j in range(i + 1, length):
                if mapping[i][1] != mapping[j][1]:
                    continue
                # make it different
                mapping[j][1] = str(i) + str(j)

                # extend target selector
                target = styleSheet.getRuleSets()[i]
                src = styleSheet.getRuleSets()[j]
                target.extendSelector(src)
                # remove rule set
                styleSheet.removeRuleSetByIndex(j)

        # remember to clean after remove ruleset
        styleSheet.clean()

    def _gen_hash(self, ruleSets):
        mapping = []
        counter = 0
        for r in ruleSets:
            if r.extra:
                # make it imposible to equal
                mapping.append(['extra', "imposible" + str(counter)])
                counter = counter + 1
                continue
            mapping.append([r.selector, r.compressRules()])
        return mapping
