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
            self.load(filePath)
    
    def load(self, filePath):
        config = ConfigParser.ConfigParser()
        f = open(filePath, 'rb')
        config.readfp(f)
        self.handleOptions(config)

    def handleOptions(self, config):
        self.handleCkStyleOptions(config)
        self.handleCompressOptions(config)
        self.handleExtraOptions(config)

    def handleExtraOptions(self, config):
        # handle other options, global-files for example
        pass

    def handleCompressOptions(self, config):
        args = self.args.compressConfig
        args.extension      = get       (config, 'compress', 'extension',       args.extension)
        args.combineFile    = getBoolean(config, 'compress', 'combine-file',    args.combineFile)
        args.browsers       = getBoolean(config, 'compress', 'browsers',        args.browsers)
        args.noBak          = getBoolean(config, 'compress', 'no-bak',          args.noBak)

    def handleCkStyleOptions(self, config):
        args = self.args
        args.errorLevel = getInt    (config, 'ckstyle', 'error-level', args.errorLevel)
        args.include    = get       (config, 'ckstyle', 'include',     args.include, True)
        args.exclude    = get       (config, 'ckstyle', 'exclude',     args.exclude, True)
        args.recursive  = getBoolean(config, 'ckstyle', 'recursive',   args.recursive)
        args.printFlag  = getBoolean(config, 'ckstyle', 'print-flag',  args.printFlag)
        args.extension  = get       (config, 'ckstyle', 'extension',   args.extension)
        args.standard   = get       (config, 'ckstyle', 'standard',    args.standard)
        args.safeMode   = getBoolean(config, 'ckstyle', 'safe-mode',   args.safeMode)
        args.noBak      = getBoolean(config, 'ckstyle', 'no-bak',      args.noBak)

        args.fixedExtension   = get       (config, 'ckstyle', 'fixed-extension',    args.fixedExtension)
        args.fixToSingleLine  = getBoolean(config, 'ckstyle', 'fix-to-single-line', args.fixToSingleLine)
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
