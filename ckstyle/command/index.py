#/usr/bin/python
#encoding=utf-8
from .ConsoleCommandParser import handleCkStyleCmdArgs, handleFixStyleCmdArgs, handleCompressCmdArgs
from .PluginManager import install, uninstall, installcmd, uninstallcmd, handleExtraCommand
import sys
from .usage import newUsage

def ckstyle():
    args = sys.argv
    if len(args) < 2:
        newUsage()
        return

    commands = {
        'check' : handleCkStyleCmdArgs,
        'fix': handleFixStyleCmdArgs,
        'compress': handleCompressCmdArgs,
        
        'install': install,
        'add': install,
        'get': install,

        'uninstall': uninstall,
        'remove': uninstall,
        'rm': uninstall,

        'installcmd': installcmd,
        'addcmd': installcmd,
        'getcmd': installcmd,

        'rmcmd': uninstallcmd,
        'removecmd': uninstallcmd,
        'uninstallcmd': uninstallcmd
    }

    subcommand = args[1]
    if commands.has_key(subcommand):
        commands.get(subcommand)(args)
    else:
        handleExtraCommand(subcommand, args)

    #handleCkStyleCmdArgs()

#def fixstyle():
#    handleFixStyleCmdArgs()

#def compress():
#    handleCompressCmdArgs()

#def main():
#    ckstyle()

if __name__ == '__main__':
    ckstyle()
