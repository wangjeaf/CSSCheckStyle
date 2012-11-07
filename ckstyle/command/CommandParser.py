import os
import string

class CommandArgs():
    def __init__(self):
        self.errorLevel = 2
        self.recursive = False
        self.exportMode = 'a'
        self.extendName = '.ckstyle.txt'
        self.include = 'all'
        self.exclude = 'none'

class CommandLineParser():
    def __init__(self, args):
        self.args = CommandArgs()
        self.commandLineArgs = args
        self.analyseCommandLineArgs()

    def analyseCommandLineArgs(self):
        pass

class CommandFileParser():
    def __init__(self):
        self.args = CommandArgs()
        self.load(os.path.realpath(os.path.join(__file__, '../.commandline')))
    
    def load(self, filePath):
        content = open(filePath).read()
        splited = content.split('\n')

        for x in splited:
            x = x.strip()
            if x.startswith('recursive'):
                value = getValue(x)
                if value.lower() == 'false':
                    self.args.recursive = False
                else:
                    self.args.recursive = True
            elif x.startswith('error-level'):
                value = getNumber(getValue(x))
                if value is None:
                    print '[ConfigError] default-error-level is not a number'
                    self.args.errorLevel = 2
                else:
                    self.args.errorLevel = value
            elif x.startswith('export'):
                value = getValue(x)
                self.args.exportMode = Mode.getMode(value)
            elif x.startswith('extend-name'):
                value = getValue(x)
                self.args.extendName = value
            elif x.startswith('include'):
                value = getValue(x)
                self.args.include = value
            elif x.startswith('exclude'):
                value = getValue(x)
                self.args.exclude = value

def getValue(txt):
    sp = txt.split(':')
    if len(sp) == 1:
        print '[ConfigError] no value after semicolon(:) '
    return sp[1].strip()

def getNumber(txt):
    value = None
    try:
        value = string.atoi(txt)
    except ValueError:
        pass
    return value

class ExportMode():
    NONE = 0
    SEPERATE = 1
    ONE_FILE = 2
    CONSOLE = 3

    @staticmethod
    def getMode(txt):
        mode = None
        if value == '-n':
            mode = ExportMode.NONE
        elif value == '-a':
            mode = ExportMode.ONE_FILE
        elif value == '-p':
            mode = ExportMode.CONSOLE
        elif value == '-s':
            mode = ExportMode.SEPERATE
        return mode
