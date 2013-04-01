#/usr/bin/python
#encoding=utf-8
import os 
import json

def loadPlugins(pluginDir):
    ids = []
    tmp = '{id:"%s", priority:%s, summary:"%s", desc:"%s", checked:%s}';

    '''从plugins目录动态载入检查类'''
    for filename in os.listdir(pluginDir):
        if not filename.endswith('.py') or filename.startswith('_'):
            continue
        if filename == 'Base.py' or filename == 'helper.py':
            continue
        pluginName = os.path.splitext(filename)[0]

        # 获取plugins的引用
        plugin = __import__("ckstyle.plugins." + pluginName, fromlist = [pluginName])
        pluginClass = None
        if hasattr(plugin, pluginName):
            pluginClass = getattr(plugin, pluginName)
        else:
            console.error('[TOOL] class %s should exist in %s.py' % (pluginName, pluginName))
            continue
        # 构造plugin的类
        instance = pluginClass()
        if (hasattr(instance, 'private') and getattr(instance, 'private') is True):
            continue
        obj = {}
        obj["id"] = instance.id
        obj["priority"] = instance.errorLevel
        obj["desc"] = pluginClass.__name__
        obj["summary"] = pluginClass.__name__
        doc = pluginClass.__doc__

        data = None
        if (doc != None):
            doc = doc.replace('\n', '')
            doc = doc.replace('\t', '')
            doc = doc.replace('  ', '')
            try:
                data = json.loads(doc)
            except Exception, e:
                print '[JSON ERROR] doc error in ' + pluginClass.__name__ + ', not json format'
                obj["desc"] = pluginClass.__doc__
        if data is not None:
            if data.has_key('summary') and data['summary'] != 'xxx':
                obj['summary'] = data['summary'].encode('utf-8')
            if data.has_key('desc') and data['desc'] != 'xxx':
                obj['desc'] = data['desc'].encode('utf-8')

        obj["checked"] = 'true' if (instance.errorLevel == 0 or instance.errorLevel == 1) else 'false'
        ids.append(tmp % (obj["id"], obj["priority"], obj["summary"], obj["desc"], obj["checked"]))

    open('D:/git/CSSCheckStyle-website/js/rules.js', 'w').write('var RULES = [\n    ' + (',\n    '.join(ids)) + '\n];');

loadPlugins('../ckstyle/plugins')