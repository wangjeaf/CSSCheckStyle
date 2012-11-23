from Base import *

class FEDUseLowerCase(RuleChecker):
    def __init__(self):
        self.id = 'lowercase-prop'
        self.errorLevel = ERROR_LEVEL.WARNING
        self.errorMsg_name = '"${name}" should use lower case, in "${selector}"'
        self.errorMsg_value = 'value of "${name}" should use lower case, in "${selector}"'
        self.errorMsg = ''

    def check(self, rule):
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
