#/usr/bin/python
#encoding=utf-8
from .ConsoleCommandParser import handleCkStyleCmdArgs, handleFixStyleCmdArgs, handleCompressCmdArgs
from .PluginManager import install, uninstall, installcmd, uninstallcmd, handleExtraCommand
import sys

usage = '''[Commands]
  ckstyle check    --options xxxx.css
  ckstyle fix      --options xxxx.css
  ckstyle compress --options xxxx.css

  ckstyle install/add/get     pluginName
  ckstyle uninstall/remove/rm pluginName

  ckstyle installcmd/addcmd/getcmd      commandName
  ckstyle uninstallcmd/removecmd/rmcmd  commandName
'''

def ckstyle():
    args = sys.argv
    if len(args) < 2:
        print(usage)
        return

    commands = {
        'check' : handleCkStyleCmdArgs,
        'fix': handleFixStyleCmdArgs,
        'compress': handleCompressCmdArgs,
        'install': install,
        'uninstall': uninstall,
        'add': install,
        'remove': uninstall,
        'addcmd': installcmd,
        'removecmd': uninstallcmd,
        'installcmd': installcmd,
        'uninstallcmd': uninstallcmd
    }

    subcommand = sys.argv[1]
    if commands.has_key(subcommand):
        commands.get(subcommand)()
    else:
        handleExtraCommand(subcommand, usage)

    #handleCkStyleCmdArgs()

#def fixstyle():
#    handleFixStyleCmdArgs()

#def compress():
#    handleCompressCmdArgs()

#def main():
#    ckstyle()

if __name__ == '__main__':
    ckstyle()
