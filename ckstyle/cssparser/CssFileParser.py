from helper import findCharFrom, handleSpecialStatement, isCommentStart, isCommentEnd, isSpecialStart, isNestedStatement
from ckstyle.entity.StyleSheet import StyleSheet

class CssParser():
    def __init__(self, roughCss = None, fileName = ''):
        self.roughCss = roughCss
        self.fileName = fileName
        self.totalLength = len(roughCss)
        self.styleSheet = StyleSheet(fileName)
        self._parseErrors = []

    def doParse(self, config = None):
        prevChar = None
        inComment = False
        length = self.totalLength
        text = self.roughCss
        selector = '';
        commentText = ''
        i = -1
        comments = []
       
        while True:
            if (i == length - 1):
                break;
            i = i + 1
            char = text[i]
            if not inComment and isCommentStart(char, text, i):
                commentText = ''
                inComment = True
            if isCommentEnd(char, text, i):
                commentText = commentText + char
                inComment = False
                comments.append(commentText)
                commentText = ''
                continue
            if inComment:
                commentText = commentText + char
                continue;
            if isSpecialStart(char):
                nextPos, attrs, operator = handleSpecialStatement(text, i, length, char)
                if nextPos is not None:
                    realComment = ''
                    if len(comments) != 0:
                        realComment = '\n'.join(comments)
                        comments = []
                    self.styleSheet.addExtraStatement(operator, char + attrs + text[nextPos], realComment)
                    i = nextPos
                    selector = ''
                    commentText = ''
                    comments = []
                    continue
            if char == '{':
                nextBracePos, attributes = findCharFrom(text, i, length, '{', '}')
                # do not need the last brace
                realComment = ''
                if len(comments) != 0:
                    realComment = '\n'.join(comments)
                    comments = []
                if isNestedStatement(selector):
                    self.styleSheet.addNestedRuleSet(selector, attributes[:-1], realComment)
                else:
                    self.styleSheet.addRuleSetByStr(selector, attributes[:-1], realComment)
                commentText = ''
                i = nextBracePos
                selector = ''
            elif char == '}':
                selector = ''
            else:
                selector = selector + char

        for ruleSet in self.styleSheet.getRuleSets():
            errors = self.doParseRules(ruleSet)
            self._parseErrors.extend(errors)

    def getParseErrors(self):
        return self._parseErrors

    def doParseRules(self, ruleSet):
        errors = []
        if ruleSet.extra:
            return errors
        text = ruleSet.roughValue
        singleLine = len(text.split('\n')) == 1
        selector = ruleSet.selector.strip()
        i = -1
        length = len(text)
        inComment = False
        collector = ''
        attr = ''
        value = ''
        valueStarted = False
        while True:
            if i == length - 1:
                break;
            i = i + 1
            char = text[i]
            if not valueStarted and isCommentStart(char, text, i):
                inComment = True
                #errors.append([-1, 'find comment in values of "%s"' % selector])
                collector = ''
            if not valueStarted and isCommentEnd(char, text, i):
                collector = ''
                inComment = False
                continue
            if not valueStarted and inComment:
                continue
            if char == ':':
                if valueStarted is True:
                    collector = collector + char
                else:
                    valueStarted = True
                    attr = collector
                    collector = ''
            elif char == ';' or char == '\n' or i == length - 1:
                valueStarted = False
                if attr == '':
                    collector = ''
                    continue
                value = collector + char
                ruleSet.addRuleByStr(selector, attr, value)
                attr = ''
                value = ''
                collector = ''
            elif char == '{':
                nextBracePos, attributes = findCharFrom(text, i, length, '{', '}')
                collector = collector + char + attributes
                i = nextBracePos
            elif char == '}':
                collector = collector + char
            elif char == '(':
                nextBracePos, attributes = findCharFrom(text, i, length, '(', ')')
                collector = collector + char + attributes
                i = nextBracePos
                # .xxx {background-image:url(xxxx)}
                if i == length - 1:
                    ruleSet.addRuleByStr(selector, attr, collector)
                    break;
            else:
                collector = collector + char

        return errors

if __name__ == '__main__':
    text = '''@media screen and (-webkit-min-device-pixel-ratio:0) {
 .publisher-c .global-publisher-selector{ top:5px;}
 .publisher-a .global-publisher-selector-status a,
 .publisher-a .global-publisher-selector-status .global-publisher-status-trigger:hover,
 .publisher-a .global-publisher-selector .active .global-publisher-status-trigger {
    background-position: 0 1px;
}
 .publisher-a .global-publisher-selector-share a,
 .publisher-a .global-publisher-selector-share a:hover,
 .publisher-a .global-publisher-selector .active .global-publisher-share-trigger{
    background-position: 0 -48px;
 }
}'''
    parser = CssParser(text)
    parser.doParse()
