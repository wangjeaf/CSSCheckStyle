class CommandArgs():
    def __init__(self):
        self.errorLevel = 2
        self.recursive = False
        self.printFlag = False
        self.extension = '.ckstyle.txt'
        self.include = 'all'
        self.exclude = 'none'
        self.standard = ''
        self.ignoreRuleSets = ['@unit-test-expecteds']
        self.fixConfig = FixArgs()
        self.compressConfig = CompressArgs()

    def __str__(self):
        return 'errorLevel: %s\n recursive: %s\n printFlag: %s\n extension: %s\n include: %s\n exclude: %s' % (self.errorLevel, self.recursive, self.printFlag, self.extension, self.include, self.exclude)

class FixArgs():
    def __init__(self):
        self.include = 'all'
        self.exclude = 'none'
        self.extension = '.fixed.css'
        self.recursive = False
        self.standard = 'standard.css'

    def __str__(self):
        return 'include: %s, exclude: %s, extension: %s, revursive: %s, standard: %s' % (self.include, self.exclude, self.extension, self.recursive, self.standard)

class CompressArgs():
    def __init__(self):
        self.recursive = False
        self.extension = '.min.css'
        self.reorder = True
        self.combineAttr = True
        self.combineRuleSet = True
        self.combineFile = True
        self.browsers = False

    def __str__(self):
        return 'recursive: %s, extension: %s, reorder: %s, combineAttr: %s, combineRuleSet: %s, combineFile: %s, browsers: %s' % (self.recursive, self.extension, self.reorder, self.combineAttr, self.combineRuleSet, self.combineFile, self.browsers)
