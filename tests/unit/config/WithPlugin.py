from helper import *

def doTest():
    _default()

def _default():
    config = parseCkStyleCmdArgs(realpath('ckstyle_with_plugin.ini'), [], [], True)
    ok(config.pluginConfig is not None, 'plugin config is not none')
    
    options = config.pluginConfig
    ok(options.has_key('plugin-a-config'), 'plugin config a')
    ok(options.has_key('plugin-b-config'), 'plugin config b')
    # config in lower case
    ok(options.has_key('pluginCConfig'), 'plugin c')

    equal(options.get('plugin-a-config'), '1', 'value of plugin config a')
    equal(options.get('plugin-b-config'), '2', 'value of plugin config b')
    equal(options.get('pluginCConfig'), '3', 'value of plugin config c')