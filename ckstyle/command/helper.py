#/usr/bin/python
#encoding=utf-8
import urllib
import os
import shutil
from ckstyle.cmdconsole.ConsoleClass import console

def realpath(a, b):
	return os.path.realpath(os.path.join(a, b))
	
debug = False
noVersion = True # do not support version currently

pluginUrl = 'https://raw.github.com/wangjeaf/ckstyle-pm/master/plugins/%s/%sindex.py'
cmdPluginUrl = 'https://raw.github.com/wangjeaf/ckstyle-pm/master/commands/%s/%sindex.py'
pluginRootDir = realpath(__file__, '../../userplugins/plugins')
cmdPluginRootDir = realpath(__file__, '../../userplugins/commands')

pluginWant = 'PluginClass'
cmdPluginWant = 'doCommand'

def getWhatIWant(pluginType):
	return pluginWant if pluginType == 'plugins' else cmdPluginWant

def fetchPlugin(name, version = ''):
	fetch(name, version, pluginUrl, pluginRootDir, 'plugins')

def fetchCmdPlugin(name, version = ''):
	return fetch(name, version, cmdPluginUrl, cmdPluginRootDir, 'commands')

def removePlugin(name, version = ''):
	remove(name, version, pluginRootDir)

def removeCmdPlugin(name, version = ''):
	remove(name, version, cmdPluginRootDir)

def remove(name, version, root):
	if noVersion:
		version = ''
	pluginDir = realpath(root, './' + name)
	if not os.path.exists(pluginDir):
		return
	if version is not None and version != '':
		versionDir = realpath(pluginDir, './v' + replacedVer)
		if not os.path.exists(versionDir):
			return
		else:
			shutil.rmtree(versionDir)
	shutil.rmtree(pluginDir)
	console.showOk('%s is removed from %s' % (name, root))
	console.showOk('Uninstall successfully!')

def findPlugin(name):
	return find(name, pluginRootDir)

def findCmdPlugin(name):
	return find(name, cmdPluginRootDir)

def find(name, root):
	pluginDir = realpath(root, './' + name)
	if not os.path.exists(pluginDir):
		return False
	filePath = realpath(pluginDir, './index.py')
	if not os.path.exists(pluginDir):
		return False
	return True

def fetch(name, version, url, root, pluginType):	
	if noVersion:
		version = ''
	
	pluginDir = realpath(root, './' + name)
	replacedVer =  '' if version == '' else version.replace('.', '_')
	if not os.path.exists(pluginDir):
		os.mkdir(pluginDir)
		open(realpath(pluginDir, './__init__.py'), 'w').write('')

	versionDir = pluginDir

	if version is not None and version != '':
		versionDir = realpath(pluginDir, './v' + replacedVer)
		if not os.path.exists(versionDir):
			os.mkdir(versionDir)
			open(realpath(versionDir, './__init__.py'), 'w').write('')
	

		
	filePath = realpath(versionDir, './index.py')

	if debug or not os.path.exists(filePath):
		realUrl = url % (name, '' if version == '' else ('' + version + '/'))
		console.showOk('Downloading %s%s from %s' % (name, version, realUrl))
		request = urllib.urlopen(realUrl)
		if request.getcode() != 200:
			console.showError('Can not download file, status code : ' + str(request.getcode()))
			return
		try:
			f = open(filePath, 'w')
			f.write(request.read())
			console.showOk('%s%s Downloaded in %s' % (name, version, filePath))
			if pluginType == 'commands':
				console.showOk('Download successfully!')
				console.showOk('Please type "ckstyle %s" to execute.' % name)
			#urllib.urlretrieve(realUrl, realUrl)
		except IOError as e:
			console.error(str(e))

	versionPath = '' if replacedVer == '' else '.v' + replacedVer

	whatIWant = getWhatIWant(pluginType)

	moduleName = "ckstyle.userplugins.%s.%s%s.index" % (pluginType, name, versionPath)
	try:
		plugin = __import__(moduleName, fromlist=["ckstyle.userplugins.%s.%s%s" % (pluginType, name, versionPath)])
	except ImportError as e:
		console.showError(('Can not import plugin %s : ' % name) + str(e))
		return

	filePath = realpath(versionDir, './index.pyc')
	if os.path.exists(filePath):
		os.remove(filePath)

	if pluginType == 'commands':
		if hasattr(plugin, 'doCommand'):
			return getattr(plugin, 'doCommand')
		else:
			console.showError('%s do not contain %s' % (moduleName, whatIWant))

	return None

if __name__ == '__main__':
	print fetchPlugin('demo')
	#print fetchPlugin('demo', '1.0')
	#print fetchCmdPlugin('democmd')
	#print fetchCmdPlugin('democmd', '1.0')
	#print removePlugin('demo')
	#print removePlugin('demo', '1.0')
	#print removeCmdPlugin('demo')
	#print removeCmdPlugin('democmd', '1.0')