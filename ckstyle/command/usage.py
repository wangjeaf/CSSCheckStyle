usage = '[Usage]'
example = '[Example]'
options = '[Options]'

fixUsage = '''
[compress]
%s
%s
%s
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
    -c / --config   specify the config file name(use "~/ckstyle.ini" as default)
    --include       specify rules(can be configed in .ini file)
    --exclude       specify exclude rules(can be configed in .ini file)
    --extension     specify check result file extension(use ".ckstyle.txt" as default)
    --errorLevel    specify error level(0-error, 1-warning, 2-log)
    ''' % (usage, example, options)

compressUsage = '''
[compress]
%s
%s
%s
    ''' % (usage, example, options)
