class CommandArgs():
    def __init__(self):
        self.errorLevel = 2
        self.recursive = False
        self.exportMode = 'a'
        self.extension = '.ckstyle.txt'
        self.include = 'all'
        self.exclude = 'none'
        self.tabSpaces = 4
        self.standard = ''
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.errorLevel, self.recursive, self.exportMode, self.extension, self.include, self.exclude, self.tabSpaces)
