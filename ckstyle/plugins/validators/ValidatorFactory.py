from ckstyle.cmdconsole.ConsoleClass import console

def doValidate(name, value):
    pluginName = camelCase(name) + 'Validator'
    pluginClass = NullValidator
    try:
        plugin = __import__('ckstyle.plugins.validators.' + pluginName, fromlist = [pluginName])
        #plugin = __import__(pluginName, fromlist = [pluginName])
        if hasattr(plugin, pluginName):
            pluginClass = getattr(plugin, pluginName)
        else:
            console.error('%s should exist in %s.py' % (pluginName, pluginName))
    except ImportError, e:
        pass
    instance = pluginClass(name, value)
    return instance.validate()

class NullValidator():
    def __init__(self, name, value):
        pass
    def validate(self):
        return True, None

def camelCase(name):
    splited = name.split('-')

    collector = []
    for x in splited:
        collector.append(x.capitalize())
    return ''.join(collector)

if __name__ == '__main__':
    print doValidate('margin', '10 10      10 10')
