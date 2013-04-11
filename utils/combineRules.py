#/usr/bin/python
#encoding=utf-8
import os 
import json

def loadPlugins(pluginDir):
    ids = []
    content = ''
    '''从plugins目录动态载入检查类'''
    for filename in os.listdir(pluginDir):
        if not filename.endswith('.py') or filename.startswith('_'):
            continue
        if filename == 'Base.py' or filename == 'helper.py':
            continue
        content = content + open(pluginDir + '/' + filename, 'r').read()

    open('AllRules.py', 'w').write(content);

loadPlugins('../ckstyle/plugins')