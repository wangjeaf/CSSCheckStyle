usage = '[Usage]'
example = '[Example]'
options = '[Options]'

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
[compress]
%s
%s
%s
    ''' % (usage, example, options)
