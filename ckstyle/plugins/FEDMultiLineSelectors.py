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

        
