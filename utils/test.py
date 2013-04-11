plugin = __import__("ckstyle.plugins.AllRules", fromlist = ['AllRules'])
props = dir(plugin)
for prop in props:
	if prop.startswith('FED'):
		print prop