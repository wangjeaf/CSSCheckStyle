import os
import ConfigParser
from ckstyle.cmdconsole.ConsoleClass import console
import args

def exists(filePath):
    return os.path.exists(filePath)

def getInt(config, group, attr, default):
    if config.has_option(group, attr):
        try:
            result = config.getint(group, attr)
            return result
        except Exception:
            console.log('%s of %s in config file should be int' % (attr, group))
    return default

def getBoolean(config, group, attr, default):
    if config.has_option(group, attr):
        try:
            result = config.getboolean(group, attr)
            return result
        except Exception:
            console.log('%s of %s in config file should be boolean' % (attr, group))
    return default

def get(config, group, attr, default, lowerFlag = False):
    if config.has_option(group, attr):
        try:
            result = config.get(group, attr)
            if lowerFlag:
                result = result.lower()
            return result
        except Exception:
            console.log('%s of %s in config file should be valid string' % (attr, group))
    return default

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
        self.handleCkStyleOptions(config)
        self.handleFixStyleOptions(config)
        self.handleCompressOptions(config)
        self.handleExtraOptions(config)

    def handleExtraOptions(self, config):
        # handle other options, global-files for example
        pass

    def handleCompressOptions(self, config):
        args = self.args.compressConfig
        args.recursive      = getBoolean(config, 'compress', 'recursive',       args.recursive)
        args.extension      = get       (config, 'compress', 'extension',       args.extension)
        args.reorder        = getBoolean(config, 'compress', 'reorder',         args.reorder)
        args.combineAttr    = getBoolean(config, 'compress', 'combine-attr',    args.combineAttr)
        args.combineRuleSet = getBoolean(config, 'compress', 'combine-ruleset', args.combineRuleSet)
        args.combineFile    = getBoolean(config, 'compress', 'combine-file',    args.combineFile)
        args.browsers       = getBoolean(config, 'compress', 'browsers',        args.browsers)

    def handleFixStyleOptions(self, config):
        args = self.args.fixConfig
        args.include   = get       (config, 'fixstyle', 'include',   args.include)
        args.exclude   = get       (config, 'fixstyle', 'exclude',   args.exclude)
        args.extension = get       (config, 'fixstyle', 'extension', args.extension)
        args.recursive = getBoolean(config, 'fixstyle', 'recursive', args.recursive)
        args.standard  = get       (config, 'fixstyle', 'standard',  args.standard)

    def handleCkStyleOptions(self, config):
        args = self.args
        args.errorLevel = getInt    (config, 'ckstyle', 'error-level', args.errorLevel)
        args.include    = get       (config, 'ckstyle', 'include',     args.include, True)
        args.exclude    = get       (config, 'ckstyle', 'exclude',     args.exclude, True)
        args.recursive  = getBoolean(config, 'ckstyle', 'recursive',   args.recursive)
        args.printFlag  = getBoolean(config, 'ckstyle', 'print-flag',  args.printFlag)
        args.extension  = get       (config, 'ckstyle', 'extension',   args.extension)
        args.standard   = get       (config, 'ckstyle', 'standard',    args.standard)
        self.handleIgnoreRuleSets(config)

    def handleIgnoreRuleSets(self, config):
        if config.has_option('ckstyle', 'ignore-rule-sets'):
            ruleSetStr = config.get('ckstyle', 'ignore-rule-sets').strip()
            if ruleSetStr.find(','):
                self.args.ignoreRuleSets = [x.strip() for x in ruleSetStr.split(',')]
            elif ruleSetStr.find(' '):
                self.args.ignoreRuleSets = [x.strip() for x in ruleSetStr.split(' ')]
            else:
                self.args.ignoreRuleSets = [ruleSetStr]
