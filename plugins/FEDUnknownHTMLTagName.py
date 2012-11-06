from Base import *
from helper import isHTMLTag

class FEDUnknownHTMLTagName(RuleSetChecker):
    def __init__(self):
        self.id = 'unknown-html-tag'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.roughErrorMsg = 'unknown html tag "${name}" found in "${selector}"'
        self.errorMsg = 'unknown html tag "${name}" found in "${selector}"'

    def check(self, ruleSet):
        selector = ruleSet.selector.lower()
        if selector.find('@media') != -1:
            return True
        if selector.find('@-moz-document') != -1:
            return True
        selectors = selector.split(',')
        for s in selectors:
            for r in s.split(' '):
                r = r.strip()
                if r != '':
                    # abcd:hover
                    # abcd.class-name:hover
                    tag = r.split(':')[0].split('.')[0].strip()

                    # .test > .inner
                    if tag == '' or tag == '>' or tag == '*' or tag == '+':
                        continue

                    # #id
                    if tag.find('#') != -1:
                        continue

                    # input[type=button]
                    if tag.find('[') != -1:
                        tag = tag.split('[')[0].strip()

                    # *+html
                    if tag.startswith('*+'):
                        tag = tag[2:]

                    # *html
                    elif tag.startswith('*'):
                        tag = tag[1:]

                    if not isHTMLTag(tag):
                        self.errorMsg = self.roughErrorMsg.replace('${name}', tag)
                        return False
        return True 
