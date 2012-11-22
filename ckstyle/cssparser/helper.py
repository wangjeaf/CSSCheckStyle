def isAlphaChar(char):
    return 97 <= ord(char) <= 122

specialTexts = [
    {'start':'@', 'text':'@import', 'end':';\n'},
    {'start':'@', 'text':'@charset', 'end':';\n'},
    {'start':'@', 'text':'@namespace', 'end':';'},
    {'start':'@', 'text':'@-css-compiler ', 'end':'}'},
    {'start':'@', 'text':'@-css-compiler-', 'end':';\n'}]

specialStartChars = set([x['start'] for x in specialTexts])

def isSpecialStart(char):
    for x in specialStartChars:
        if x == char:
            return True
    return False

def handleSpecialStatement(text, i, length, char):
    for obj in specialTexts:
        if char == obj['start'] and isSpecialString(text, i, obj["text"]):
            a, b = findCharFrom(text, i, length, obj["end"])
            return a, b, obj["text"]
    return None, None, None

def findCharFrom(text, i, length, left, right = None):
    counter = 1
    collector = ''
    for j in range(i + 1, length):
        if right == None:
            if text[j] == left or left.find(text[j]) != -1:
                break;
            else:
                collector = collector + text[j]
        else:
            if text[j] == left:
                collector = collector + text[j]
                counter = counter + 1
            elif text[j] == right:
                collector = collector + text[j]
                counter = counter - 1
                if counter == 0:
                    break;
            else:
                collector = collector + text[j]
    return j, collector

def isSpecialString(text, i, string):
    return text[i: i + len(string)] == string

def isCommentStart(char, text, i):
    return char == '/' and i + 1 < len(text) and text[i + 1] == '*'

def isCommentEnd(char, text, i):
    return char == '/' and text[i - 1] == '*'

