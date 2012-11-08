#/usr/bin/python
#encoding=utf-8

import os

from plugins.Base import *

class CssChecker():
    '''CSS检查类，需要CSS解析器作为辅助'''
    def __init__(self, parser):
        self.parser = parser

        # 错误记录，log是2级，warn是1级，error是0级
        self.logMsgs = []
        self.warningMsgs = []
        self.errorMsgs = []

        # 额外的错误记录，比如工具内部的一些错误等
        self.extraMsgs = []

        # 注册的不同类型的检查器（都来自plugins目录）
        self.ruleSetCheckers = []
        self.ruleCheckers = []
        self.styleSheetCheckers = []

        # 如果有解析过程的错误，则先把那些错误记录下来
        self.handleParseErrors()

    def getStyleSheet(self):
        '''获取styleSheet引用'''
        return self.parser.styleSheet

    def handleParseErrors(self):
        for msg in self.parser.getParseErrors():
            self.remember(msg[0], msg[1])

    def hasError(self):
        '''判断是否有error'''
        return len(self.logMsgs) != 0 or len(self.warningMsgs) != 0 or len(self.errorMsgs) != 0

    def errors(self):
        '''把错误信息导出'''
        return self.logMsgs, self.warningMsgs, self.errorMsgs

    def loadPlugins(self, pluginDir):
        '''从plugins目录动态载入检查类'''
        # ids = {}
        for filename in os.listdir(pluginDir):
            if not filename.endswith('.py') or filename.startswith('_'):
                continue
            if filename == 'Base.py' or filename == 'helper.py':
                continue
            pluginName = os.path.splitext(filename)[0]

            # 获取plugins的引用
            plugin = __import__("ckstyle.plugins." + pluginName, fromlist = [pluginName])
            pluginClass = None
            if hasattr(plugin, pluginName):
                pluginClass = getattr(plugin, pluginName)
            else:
                print '[TOOL] class %s should exist in %s.py' % (pluginName, pluginName)
                continue
            # 构造plugin的类
            instance = pluginClass()
            # ids[instance.id] = pluginName
            if instance.errorMsg.find(';') != -1 or instance.errorMsg.find('\n') != -1:
                print r'[TOOL] errorMsg should not contain ";" or "\n" in %s.py' % pluginName
                continue

            # 注册到检查器中
            self.registerChecker(instance)

    def registerChecker(self, checker):
        '''根据检查器类型的不同，分别注册到不同的检查器列表中'''
        if isinstance(checker, RuleChecker):
            self.registerRuleChecker(checker)
        elif isinstance(checker, RuleSetChecker):
            self.registerRuleSetChecker(checker)
        else:
            self.registerStyleSheetChecker(checker)

    def registerStyleSheetChecker(self, checker):
        self.styleSheetCheckers.append(checker)

    def registerRuleSetChecker(self, checker):
        self.ruleSetCheckers.append(checker)

    def registerRuleChecker(self, checker):
        self.ruleCheckers.append(checker)

    def remember(self, errorLevel, errorMsg):
        '''记录代码中的问题'''
        if errorLevel == ERROR_LEVEL.LOG:
            self.logMsgs.append(errorMsg)
        elif errorLevel == ERROR_LEVEL.WARNING:
            self.warningMsgs.append(errorMsg)
        elif errorLevel == ERROR_LEVEL.ERROR:
            self.errorMsgs.append(errorMsg)
        else:
            print '[TOOL] wrong ErrorLevel for ' + errorMsg

    def logStyleSheetMessage(self, checker, styleSheet):
        '''记录StyleSheet的问题'''
        errorLevel = checker.getLevel()
        errorMsg = checker.getMsg()
        if errorMsg is None or errorMsg == '':
            print '[TOOL] no errorMsg in your plugin, please check it'
        if errorMsg.find('${file}') == -1:
            errorMsg = errorMsg + ' (from "' + styleSheet.getFile() + '")'
        else:
            errorMsg = errorMsg.replace('${file}', styleSheet.getFile())
        self.remember(errorLevel, errorMsg);

    def logRuleMessage(self, checker, rule):
        '''记录一条key/value的问题'''
        errorLevel = checker.getLevel()
        errorMsg = checker.getMsg()
        if errorMsg is None or errorMsg == '':
            print '[TOOL] no errorMsg in your plugin, please check it'
        if errorMsg.find('${selector}') == -1:
            errorMsg = errorMsg + ' (from "' + rule.selector + '")'
        else:
            errorMsg = errorMsg.replace('${selector}', rule.selector)
        errorMsg = errorMsg.replace('${name}', rule.roughName.strip())
        errorMsg = errorMsg.replace('${value}', rule.value.strip())
        self.remember(errorLevel, errorMsg);

    def logRuleSetMessage(self, checker, ruleSet):
        '''记录一个"规则集"中的问题'''
        errorLevel = checker.getLevel()
        errorMsg = checker.getMsg()
        if errorMsg.find('${selector}') == -1:
            errorMsg = errorMsg + ' (from "' + ruleSet.selector + '")'
        else:
            errorMsg = errorMsg.replace('${selector}', ruleSet.selector)
        self.remember(errorLevel, errorMsg);

    def doCheck(self):
        # 忽略的规则集（目前只忽略单元测试的selector）
        ignoreRuleSets = ['@unit-test-expecteds']
        def findInArray(array, value):
            for x in array:
                if x == value:
                    return True
            return False

        # 检查规则集
        def checkRuleSet(ruleSet):
            for checker in self.ruleSetCheckers:
                if not checker.check(ruleSet):
                    self.logRuleSetMessage(checker, ruleSet)

        # 检查规则
        def checkRule(ruleSet):
            for checker in self.ruleCheckers:
                for rule in ruleSet._rules:
                    if not checker.check(rule):
                        self.logRuleMessage(checker, rule)

        # 检查样式表
        styleSheet = self.parser.styleSheet
        for checker in self.styleSheetCheckers:
            if not checker.check(styleSheet):
                self.logStyleSheetMessage(checker, styleSheet)

        for ruleSet in styleSheet.getRuleSets():
            # 判断此规则是否忽略
            if findInArray(ignoreRuleSets, ruleSet.selector):
                continue
            checkRuleSet(ruleSet)
            checkRule(ruleSet)
