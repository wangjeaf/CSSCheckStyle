class CommandArgs():
    def __init__(self):
        self.errorLevel = 2
        self.recursive = False
        self.printFlag = False
        self.extension = '.ckstyle.txt'
        self.include = 'all'
        self.exclude = 'none'
        self.tabSpaces = 4
        self.standard = ''
        self.ignoreRuleSets = ['@unit-test-expecteds']

    def __str__(self):
        return 'errorLevel: %s\n recursive: %s\n printFlag: %s\n extension: %s\n include: %s\n exclude: %s\n tabSpaces:%s' % (self.errorLevel, self.recursive, self.printFlag, self.extension, self.include, self.exclude, self.tabSpaces)
