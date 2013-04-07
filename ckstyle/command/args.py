class CommandArgs():
    def __init__(self):
        self.operation = None
        self.errorLevel = 2
        self.recursive = False
        self.printFlag = False
        self.extension = '.ckstyle.txt'
        self.include = 'all'
        self.exclude = 'none'
        self.standard = ''
        self.exportJson = False
        self.ignoreRuleSets = ['@unit-test-expecteds']
        self.fixedExtension = '.fixed.css'
        self.fixToSingleLine = False
        self.compressConfig = CompressArgs()
        self.safeMode = False
        self.noBak = False

    def __str__(self):
        return 'errorLevel: %s\n recursive: %s\n printFlag: %s\n extension: %s\n include: %s\n exclude: %s' % (self.errorLevel, self.recursive, self.printFlag, self.extension, self.include, self.exclude)

class CompressArgs():
    def __init__(self):
        self.extension = '.min.css'
        self.combineFile = True
        self.browsers = None
        self.noBak = False

    def __str__(self):
        return 'extension: %s, combineFile: %s, browsers: %s' % (self.recursive, self.extension, self.combineAttr, self.combineRuleSet, self.combineFile, self.browsers)
