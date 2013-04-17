#/usr/bin/python
#encoding=utf-8

import sys
from .helper import fetchPlugin, fetchCmdPlugin, removePlugin, removeCmdPlugin, findCmdPlugin

def getNameAndVersion():
	args = sys.argv
	argLen = len(args)
	if argLen < 3 or argLen > 4:
		print '[CKstyle ERROR] wrong arg length, use "ckstyle -h" to see help.'
		return None, None
	pluginName = args[2]
	version = ''
	if argLen == 4:
		version = args[3]

	return pluginName, version

def install():
	pluginName, version = getNameAndVersion()
	if pluginName is None:
		return
	fetchPlugin(pluginName, version)

def uninstall():
	pluginName, version = getNameAndVersion()
	if pluginName is None:
		return
	removePlugin(pluginName, version)

def installcmd():
	pluginName, version = getNameAndVersion()
	if pluginName is None:
		return
	fetchCmdPlugin(pluginName, version)

def uninstallcmd():
	pluginName, version = getNameAndVersion()
	if pluginName is None:
		return
	removeCmdPlugin(pluginName, version)

def handleExtraCommand(command, usage):
	if command.startswith('-') or command.startswith('.'):
		print(usage)
		return
	if not findCmdPlugin(command):
		print('[CKstyle ERROR] CKstyle can not find the subcommand: "%s".' % command)
		print('[CKstyle ERROR] Maybe you can type "ckstyle installcmd %s" to install this command from ckstyle-pm.' % command)
		return
	cmd = fetchCmdPlugin(command)
	if cmd is None:
		return
	cmd()
