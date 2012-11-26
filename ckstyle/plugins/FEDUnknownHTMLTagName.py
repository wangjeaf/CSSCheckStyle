from Base import *
from helper import isHTMLTag, isKeyFrames

class FEDUnknownHTMLTagName(RuleSetChecker):
    def __init__(self):
        self.id = 'unknown-html-tag'
        self.errorLevel = ERROR_LEVEL.ERROR
        self.errorMsg_rough = 'unknown html tag "%s" found in "${selector}"'
        self.errorMsg = ''

    def check(self, ruleSet, config):
        selector = ruleSet.selector.lower()
        if selector.find('@media') != -1:
            return True
        if selector.find('@-moz-document') != -1:
            return True
        if isKeyFrames(selector):
            return True
        selectors = selector.split(',')
        for s in selectors:
            for r in s.split(' '):
                r = r.strip()
                if r != '':
                    if r.find('::') != -1:
                        # p::selection
                        tag = r.split('::')[0].split('.')[0].split('#')[0].strip()
                    else:
                        # abcd:hover
                        # abcd.class-name:hover
                        # abcd#class-name:hover
                        tag = r.split(':')[0].split('.')[0].split('#')[0].strip()

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
                        self.errorMsg = self.errorMsg_rough % tag
                        return False
        return True 
