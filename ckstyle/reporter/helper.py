
def fill(obj):
	def fillRuleSet( obj):
	    errorMsg = obj["errorMsg"]
	    if errorMsg.find('${selector}') == -1:
	        errorMsg = errorMsg + ' (from "' + obj["selector"] + '")'
	    else:
	        errorMsg = errorMsg.replace('${selector}', obj["selector"])
	    return errorMsg

	def fillStyleSheet( obj):
	    errorMsg = obj["errorMsg"]
	    if errorMsg.find('${file}') == -1:
	        errorMsg = errorMsg + ' (from "' + obj["file"] + '")'
	    else:
	        errorMsg = errorMsg.replace('${file}', obj["file"])
	    return errorMsg

	def fillRule(obj):
	    errorMsg = obj["errorMsg"]
	    if errorMsg.find('${selector}') == -1:
	        errorMsg = errorMsg + ' (from "' + obj["selector"] + '")'
	    else:
	        errorMsg = errorMsg.replace('${selector}', obj["selector"])
	    errorMsg = errorMsg.replace('${name}', obj["name"])
	    errorMsg = errorMsg.replace('${value}', obj["value"])
	    return errorMsg

	level = obj["level"]
	if level == 'rule':
	    return fillRule(obj)
	elif level == 'ruleset':
	    return fillRuleSet(obj)
	elif level == 'stylesheet':
	    return fillStyleSheet(obj)
	return obj["errorMsg"]