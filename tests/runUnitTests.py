import os
import string
import datetime
from ckstyle.cmdconsole.ConsoleClass import console
from ckstyle.plugins.Base import *
from ckstyle.doCssCheck import doCheck

def realpath(directory, fileName):
    return os.path.realpath(os.path.join(directory, fileName))

def fillDicts(logs, warnings, errors, expectedErrors):
    for expected in expectedErrors:
        level = string.atoi(expected.name.strip())
        value = expected.value.split('(from ')[0].strip()

        if level == ERROR_LEVEL.LOG:
            logs[value] = 1
        elif level == ERROR_LEVEL.WARNING:
            warnings[value] = 1
        elif level == ERROR_LEVEL.ERROR:
            errors[value] = 1

def checkUnitTestResult(expecteds, reals, level, fileName):
    global okCounter
    global errorCounter
    for real in reals:
        real = real.split('(from "')[0].strip()
        if expecteds.has_key(real):
            okCounter = okCounter + 1
            expecteds[real] = 0
        else:
            errorCounter = errorCounter + 1
            console.show('[UnitTest] [unexpected but has] level ' + level + '( ' + real + ' )' + ' in ' + fileName)

    for key, value in expecteds.items():
        if value == 1:
            errorCounter = errorCounter + 1
            console.show('[UnitTest] [expect but has not] level ' + level + '( ' + key + ' )' + ' in ' + fileName)

errorCounter = 0;
okCounter = 0;
fileCounter = 0;

def doCheckWithPythonFile(f, module):
    global fileCounter, okCounter, errorCounter

    caseName = os.path.splitext(f)[0]
    plugin = __import__(module + caseName, fromlist = [module + caseName])
    pluginMethod = None
    if hasattr(plugin, 'doTest'):
        pluginMethod = getattr(plugin, 'doTest')
    else:
        console.error('doTest should exist in %s' % f)
    if pluginMethod is None:
        return

    pluginMethod()

    getResults = None
    if hasattr(plugin, 'getResults'):
        getResults = getattr(plugin, 'getResults')
    else:
        console.error('[TOOL] %s should import asserts.py' % f)
    if getResults is None:
        return

    fileCounter = fileCounter + 1

    results = getResults()

    for result in results:
        if result[0] == False:
            errorCounter = errorCounter + 1
            console.show('[UnitTest] [' + f + ']' + result[1])
        else:
            okCounter = okCounter + 1

def fullsplit(path, result=None):
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

def runTestsInDir(filePath, module):
    global fileCounter
    for filename in os.listdir(filePath):
        if (os.path.isdir(os.path.join(filePath, filename))):
            runTestsInDir(os.path.join(filePath, filename), module + filename + '.')
            continue

        if filename == 'asserts.py' or filename == 'helper.py' or filename.startswith('_'):
            continue
        if filename.endswith('.py'):
            doCheckWithPythonFile(filename, module)
            continue
        if not filename.endswith('.css'):
            continue
        testFileName = realpath(filePath, filename)
        fileContent = open(testFileName).read()
        checker = doCheck(fileContent, filename)

        styleSheet = checker.getStyleSheet()

        testErrorSet = styleSheet.getRuleSetBySelector('@unit-test-expecteds')
        if testErrorSet is None:
            console.error('no @unit-test-expecteds in %s' % testFileName)
            continue
        expectedErrors = testErrorSet.getRules()
        if expectedErrors is None:
            console.error('no error instance in @unit-test-expecteds, %s' % testFileName)
            continue

        fileCounter = fileCounter + 1

        logs = {}
        errors = {}
        warnings = {}
        fillDicts(logs, warnings, errors, expectedErrors)

        realLogs, realWarnings, realErrors = checker.errors()

        checkUnitTestResult(logs, realLogs, '2', filename)
        checkUnitTestResult(warnings, realWarnings, '1', filename)
        checkUnitTestResult(errors, realErrors, '0', filename)


def runUnitTests():
    global fileCounter
    filePath = realpath(__file__, '../unit')

    start = datetime.datetime.now()
    runTestsInDir(filePath, 'unit.')
    end = datetime.datetime.now()

    delta = (end - start).microseconds / 1000
    console.show('[UnitTest] error: %s, pass: %s, in %s files, costs %s ms' % (errorCounter, okCounter, fileCounter, delta))

if __name__ == '__main__':
    runUnitTests()
