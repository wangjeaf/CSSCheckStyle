from Base import *

class FED16ColorShouldUpper(RuleChecker):
    def __init__(self):
        self.id = 'hexadecimal-color'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_length = 'wrong color length(should be 3 or 6) in "${selector}"'
        self.errorMsg_replace = 'replace "#${from}" with "#${to}" in "${selector}"'
        self.errorMsg_upper = 'color should in upper case in "${selector}"'
        self.errorMsg = ''

    def check(self, rule):
        value = rule.value
        if value.find('#') == -1:
            return True

        found = self._findColor(rule.value)

        if self._isLower(found):
            self.errorMsg = self.errorMsg_upper
            return False

        if len(found) == 3:
            return True

        if self._wrongLength(found):
            self.errorMsg = self.errorMsg_length
            return False

        if self._isDuplicate(found):
            self.errorMsg = self.errorMsg_replace.replace('${from}', found).replace('${to}', found[0]+found[2]+found[4])
            return False
        
        return True

    def fix(self, rule):
        value = rule.fixedValue
        if value.find('#') == -1:
            return

        found = self._findColor(rule.fixedValue)

        if self._isLower(found):
            rule.fixedValue = rule.fixedValue.replace('#' + found, '#' + found.upper())
            found = found.upper()

        if len(found) == 3:
            return

        if self._wrongLength(found):
            final = found[0:6] if len(found) > 6 else (found + (6 - len(found)) * 'F')
            rule.fixedValue = rule.fixedValue.replace('#' + found, '#' + final)
            found = final

        if self._isDuplicate(found):
            rule.fixedValue = rule.fixedValue.replace('#' + found, '#' + found[0] + found[2] + found[4])

    def _wrongLength(self, found):
        return len(found) != 3 and len(found) != 6

    def _isLower(self, found):
        return found != found.upper()

    def _isDuplicate(self, found):
        return found[0] == found[1] and found[2] == found[3] and found[4] == found[5]

    def _findColor(self, value):
        splited = value.split(' ')
        found = None
        for x in splited:
            if x.startswith('#'):
                found = x
                break
        if found is not None:
            found = found[1:]
        return found
