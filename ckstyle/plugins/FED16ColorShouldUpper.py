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

        splited = value.split(' ')
        found = None
        for x in splited:
            if x.find('#') != -1:
                found = x
                break

        found = found.strip()[1:]

        if found != found.upper():
            self.errorMsg = self.errorMsg_upper
            return False

        if len(found) == 3:
            return True

        if len(found) != 6:
            self.errorMsg = self.errorMsg_length
            return False

        if found[0] == found[1] and found[2] == found[3] and found[4] == found[5]:
            self.errorMsg = self.errorMsg_replace.replace('${from}', found).replace('${to}', found[0]+found[2]+found[4])
            return False
        
        return True
