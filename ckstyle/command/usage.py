#/usr/bin/python
#encoding=utf-8

from .helper import cmdPluginRootDir, fetchCmdPlugin
import os

usage = '[Usage]'
example = '[Example]'
options = '[Options]'


newUsageBase = '''
  [Commands]
  
   - ckstyle check    --options xxxx.css
   - ckstyle fix      --options xxxx.css
   - ckstyle compress --options xxxx.css

   - ckstyle install/add/get      [pluginName]
   - ckstyle uninstall/remove/rm  [pluginName]

   - ckstyle installcmd/addcmd/getcmd      [commandName]
   - ckstyle uninstallcmd/removecmd/rmcmd  [commandName]
'''

def newUsage():
    extraUsage = ''
    for f in os.listdir(cmdPluginRootDir):
        if f.startswith('__') or f.endswith('.py') or f.endswith('.pyc'):
            continue
        realPath = os.path.realpath(os.path.join(cmdPluginRootDir, f))
        if os.path.isdir(realPath) and fetchCmdPlugin(f) is not None:
            if extraUsage == '':
                  extraUsage = '  [Installed Cmds]\n\n'
            extraUsage = extraUsage + '   - ckstyle ' + f
    if extraUsage != '':
        extraUsage = '\n' + extraUsage
    print newUsageBase + extraUsage + '\n'

compressUsage = '''
[compress]
%s
    Compress shares almost the same options with ckstyle, but has more.

    compress -h / compress --help
    compress file.css
    compress -r dir
    compress -r -p dir

    compress --browsers=true dirpath
    compress --compressExtension=.min1.css dirpath

    compress -r --combineFile=all.min.css dirpath (coming soon)
    compress a.css b.css c.css to all.min.css (coming soon)

%s
    compress -r -p -c xxx.ini --compressExtension=.min2.css --include=all --exclude=none --browsers=true dirpath

%s
    -h / --help     show help
    -r              compress files in directory recursively
    -p              print compressed file content to console(delete result files at the same time)
    -c / --config   specify the config file name(use ckstyle.ini or ~/ckstyle.ini as default)
    --include       specify rules(can be configed in .ini file)
    --exclude       specify exclude rules(can be configed in .ini file)
    --compressExtension     specify compressed file extension(use ".min.css" as default)
    --browsers      compress css for different browsers, generate .ie6.css/.ie7.css/std.css/all.css ...
    --combineFile   combine all compressed css content into a file (todo)
    ''' % (usage, example, options)

ckstyleUsage = '''
[ckstyle]
%s
    ckstyle -h / ckstyle --help
    ckstyle
    ckstyle file.css
    ckstyle dir 
    ckstyle -r dir
    ckstyle -p -r dir
    ckstyle -c xxx.ini 
    ckstyle -c xxx.ini -r -p

%s
    ckstyle -r -p -c xxx.ini --extension=.test.txt --include=all --exclude=none --errorLevel=2 dirpath

%s
    -h / --help     show help
    -r              check files in directory recursively
    -p              print check result to console(delete result files at the same time)
    -c / --config   specify the config file name(use ckstyle.ini or ~/ckstyle.ini as default)
    --include       specify rules(can be configed in .ini file)
    --exclude       specify exclude rules(can be configed in .ini file)
    --extension     specify check result file extension(use ".ckstyle.txt" as default)
    --errorLevel    specify error level(0-error, 1-warning, 2-log)
    ''' % (usage, example, options)

fixUsage = '''
[fixstyle]
%s
    Fixstyle shares almost the same options with ckstyle, but has more.

    fixstyle -h / fixstyle --help
    fixstyle file.css
    fixstyle -r dir
    fixstyle -r -p dir

    fixstyle --fixedExtension=.fixed2.css dirpath
    fixstyle --singleLine dirpath

%s
    fixstyle -r -p -c xxx.ini --fixedExtension=.test.txt --include=all --exclude=none dirpath

%s
    -h / --help     show help
    -r              fix files in directory recursively
    -p              print fixed file content to console(delete result files at the same time)
    -c / --config   specify the config file name(use ckstyle.ini or ~/ckstyle.ini as default)
    --include       specify rules(can be configed in .ini file)
    --exclude       specify exclude rules(can be configed in .ini file)
    --fixedExtension     specify fixed file extension(use ".fixed.css" as default)
    --singleLine    fix all rule sets to single line mode
    ''' % (usage, example, options)
