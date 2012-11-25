import os
import ConfigParser
from ckstyle.cmdconsole.ConsoleClass import console
import args

def exists(filePath):
    return os.path.exists(filePath)

class CommandFileParser():
    def __init__(self, filePath, debug = False):
        self.args = args.CommandArgs()
        if exists(filePath):
            if not debug:
                console.log('load config from %s' % filePath)
            self.load(filePath)
        else:
            if not debug:
                console.log('no config file specified, will use default settings.')
    
    def load(self, filePath):
        config = ConfigParser.ConfigParser()
        f = open(filePath, 'rb')
        config.readfp(f)
        self.handleOptions(config)

    def handleOptions(self, config):
        if config.has_option('ckstyle', 'error-level'):
            self.args.errorLevel = config.getint('ckstyle', 'error-level')

        if config.has_option('ckstyle', 'include'):
            self.args.include = config.get('ckstyle', 'include').lower()

        if config.has_option('ckstyle', 'exclude'):
            self.args.exclude = config.get('ckstyle', 'exclude').lower()

        if config.has_option('ckstyle', 'recursive'):
            self.args.recursive = config.getboolean('ckstyle', 'recursive')

        if config.has_option('ckstyle', 'print-flag'):
            self.args.printFlag = config.getboolean('ckstyle', 'print-flag')

        if config.has_option('ckstyle', 'extension'):
            self.args.extension = config.get('ckstyle', 'extension')

        if config.has_option('ckstyle', 'tab-spaces'):
            self.args.tabSpaces = config.getint('ckstyle', 'tab-spaces')

        if config.has_option('ckstyle', 'standard'):
            self.args.standard = config.get('ckstyle', 'standard')

        if config.has_option('ckstyle', 'ignore-rule-sets'):
            ruleSetStr = config.get('ckstyle', 'ignore-rule-sets').strip()
            if ruleSetStr.find(','):
                self.args.ignoreRuleSets = [x.strip() for x in ruleSetStr.split(',')]
            elif ruleSetStr.find(' '):
                self.args.ignoreRuleSets = [x.strip() for x in ruleSetStr.split(' ')]
            else:
                self.args.ignoreRuleSets = [ruleSetStr]
