import os
import ConfigParser
import args

def exists(filePath):
    return os.path.exists(filePath)

class CommandFileParser():
    def __init__(self, filePath):
        self.args = args.CommandArgs()
        if exists(filePath):
            self.load(filePath)
        else:
            print '[error] file "%s" does not exist, will use default settings.' % filePath
    
    def load(self, filePath):
        config = ConfigParser.ConfigParser()
        f = open(filePath, 'rb')
        config.readfp(f)
        self.handleOptions(config)

    def handleOptions(self, config):
        if config.has_option('config', 'error-level'):
            self.args.errorLevel = config.getint('config', 'error-level')

        if config.has_option('config', 'include'):
            self.args.include = config.get('config', 'include').lower()

        if config.has_option('config', 'exclude'):
            self.args.exclude = config.get('config', 'exclude').lower()

        if config.has_option('config', 'recursive'):
            self.args.recursive = config.getboolean('config', 'recursive')

        if config.has_option('config', 'print-flag'):
            self.args.printFlag = config.getboolean('config', 'print-flag')

        if config.has_option('config', 'extension'):
            self.args.extension = config.get('config', 'extension')

        if config.has_option('config', 'tab-spaces'):
            self.args.tabSpaces = config.getint('config', 'tab-spaces')

        if config.has_option('config', 'standard'):
            self.args.standard = config.get('config', 'standard')

        if config.has_option('config', 'ignore-rule-sets'):
            ruleSetStr = config.get('config', 'ignore-rule-sets').strip()
            if ruleSetStr.find(','):
                self.args.ignoreRuleSets = [x.strip() for x in ruleSetStr.split(',')]
            elif ruleSetStr.find(' '):
                self.args.ignoreRuleSets = [x.strip() for x in ruleSetStr.split(' ')]
            else:
                self.args.ignoreRuleSets = [ruleSetStr]
