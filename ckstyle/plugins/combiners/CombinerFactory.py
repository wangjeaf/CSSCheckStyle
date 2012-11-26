def getCombiner(name, props):
    pluginName = camelCase(name) + 'Combiner'
    plugin = __import__(pluginName, fromlist = [pluginName])
    pluginClass = None
    if hasattr(plugin, pluginName):
        pluginClass = getattr(plugin, pluginName)
    else:
        return
    instance = pluginClass(name, props)
    print instance.combine()

def camelCase(name):
    splited = name.split('-')

    collector = []
    for x in splited:
        collector.append(x.capitalize())
    return ''.join(collector)

if __name__ == '__main__':
    getCombiner('margin', [
        ['margin', 'margin', '10px'],
        ['margin-left', 'margin-left', '0px'],
        ['margin-right', 'margin-right', '10px'],
        ['margin-top', 'margin-top', '10px'],
        ['margin-bottom', 'margin-bottom', '10px'],
        ['margin-bottom', 'margin-bottom', '30px']
    ])
