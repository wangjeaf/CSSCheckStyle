#/usr/bin/python
#encoding=utf-8

from .Base import *

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
