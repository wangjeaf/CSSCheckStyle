import sys
import os
from ckstyle.doCssCheck import doCheck
from ckstyle.doCssFix import doFix
from ckstyle.doCssCompress import doCompress
from ckstyle.reporter.ReporterUtil import ReporterUtil
from ckstyle.cssparser.CssFileParser import CssParser
from ckstyle.entity.StyleSheet import StyleSheet

def checkCssFileByOpm(filePath):
    fileContent = open(filePath).read()
    checker = doCheck(fileContent, filePath)
    if checker.hasError():
        reporter = ReporterUtil.getReporter('text', checker)
        reporter.doReport()
        print reporter.export()
        return False
    return True

def fixCss(filePath):
    fileContent = open(filePath).read()
    checker = doFix(fileContent, filePath)
    print checker.parser.styleSheet.getRuleSets()[0].values
    print checker.parser.styleSheet.getRuleSets()[0].getRules()[0].fixedValue

def compressCss(filePath):
    fileContent = open(filePath).read()
    checker, content = doCompress(fileContent, filePath)
    print content

if __name__ == '__main__':
    dirpath = 'smallsite'
    content = ''
    for f in os.listdir(dirpath):
        selectors = {}
        path = dirpath + '/' + f
        parser = CssParser(open(path, 'r').read(), f)
        parser.doParse()
        for ruleSet in parser.styleSheet._ruleSets:
            selector = ruleSet.selector
            splited = selector.split(',')
            for x in splited:
                x = x.strip()
                if x == '':
                    continue
                if selectors.has_key(x):
                    selectors[x].append(f)
                else:
                    selectors[x] = [f]
        for name, value in selectors.items():
            if len(value) > 2:
                content = content + name + " =====> " + value[0] + "(" + str(len(value)) + 'times)\n'

    open('result.txt', 'w').write(content)

    #path = os.path.realpath(os.path.join(__file__, '../test.css'))
    #checkCssFileByOpm(path)
    #fixCss('test.css')
    #compressCss(path)
