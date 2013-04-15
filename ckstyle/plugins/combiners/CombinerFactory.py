from ckstyle.cmdconsole.ConsoleClass import console

def doCombine(name, props):
    pluginName = camelCase(name) + 'Combiner'
    pluginClass = NullCombiner
    try:
        plugin = __import__('ckstyle.plugins.combiners.' + pluginName, fromlist = [pluginName])
        if hasattr(plugin, pluginName):
            pluginClass = getattr(plugin, pluginName)
        else:
            console.error('%s should exist in %s.py' % (pluginName, pluginName))
    except ImportError as e:
        pass
    instance = pluginClass(name, props)
    return instance.combine()

class NullCombiner():
    def __init__(self, name, props):
        pass
    def combine(self):
        return None, [], False

def camelCase(name):
    splited = name.split('-')

    collector = []
    for x in splited:
        collector.append(x.capitalize())
    return ''.join(collector)

if __name__ == '__main__':
    print doCombine('margin', [
        ['margin', 'margin', '50px auto 0 auto']
    ])
