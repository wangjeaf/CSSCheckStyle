#/usr/bin/python
#encoding=utf-8

import sys
from ckstyle.cmdconsole.ConsoleClass import console
from .helper import fetchPlugin, fetchCmdPlugin, removePlugin, removeCmdPlugin, findCmdPlugin
from .usage import newUsage

def getNameAndVersion(args):
	argLen = len(args)
	if argLen < 3 or argLen > 4:
		console.error('wrong arg length, use "ckstyle -h" to see help.')
		return None, None
	pluginName = args[2]
	version = ''
	if argLen == 4:
		version = args[3]

	return pluginName, version

def install(args):
	pluginName, version = getNameAndVersion(args)
	if pluginName is None:
		return
	fetchPlugin(pluginName, version)

def uninstall(args):
	pluginName, version = getNameAndVersion(args)
	if pluginName is None:
		return
	removePlugin(pluginName, version)

def installcmd(args):
	pluginName, version = getNameAndVersion(args)
	if pluginName is None:
		return
	fetchCmdPlugin(pluginName, version)

def uninstallcmd(args):
	pluginName, version = getNameAndVersion(args)
	if pluginName is None:
		return
	removeCmdPlugin(pluginName, version)

def handleExtraCommand(command, args):
	if command.startswith('-') or command.startswith('.'):
		newUsage()
		return
	if not findCmdPlugin(command):
		console.show('[CKstyle ERROR] CKstyle can not find the subcommand: "%s".' % command)
		console.show('[CKstyle ERROR] Maybe you can type "ckstyle installcmd %s" to install this command from ckstyle-pm.' % command)
		return
	cmd = fetchCmdPlugin(command)
	if cmd is None:
		return
	cmd()
