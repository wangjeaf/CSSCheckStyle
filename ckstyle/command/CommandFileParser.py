import os
import ConfigParser
import CommandArgs

def exists(filePath):
    return os.path.exists(filePath)

class CommandFileParser():
    def __init__(self, filePath):
        self.args = CommandArgs.CommandArgs()
        if exists(filePath):
            self.load(filePath)
        else:
            print '[error] file %s does not exist' % filePath
    
    def load(self, filePath):
        config = ConfigParser.ConfigParser()
        f = open(filePath, 'rb')
        config.readfp(f)
        self.handleOptions(config)

    def handleOptions(self, config):
        if config.has_option('config', 'error-level'):
            self.args.errorLevel = config.getint('config', 'error-level')
        if config.has_option('config', 'include'):
            self.args.include = config.get('config', 'include')
        if config.has_option('config', 'exclude'):
            self.args.include = config.get('config', 'exclude')
        if config.has_option('config', 'recursive'):
            self.args.recursive = config.getboolean('config', 'recursive')
        if config.has_option('config', 'export'):
            self.args.recursive = config.get('config', 'export')
        if config.has_option('config', 'extension'):
            self.args.extension = config.get('config', 'extension')
        if config.has_option('config', 'tab-spaces'):
            self.args.tabSpaces = config.getint('config', 'tab-spaces')
        if config.has_option('config', 'standard'):
            self.args.standard = config.get('config', 'standard')
