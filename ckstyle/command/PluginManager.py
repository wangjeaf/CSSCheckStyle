#/usr/bin/python
#encoding=utf-8

import sys
from .helper import fetchPlugin, fetchCmdPlugin, removePlugin, removeCmdPlugin, findCmdPlugin

def getNameAndVersion():
	args = sys.argv
	argLen = len(args)
	if argLen < 3 or argLen > 5:
		print '[usage] ckstyle install pluginName version'
		return
	pluginName = args[2]
	version = ''
	if argLen == 4:
		version = args[3]

	return pluginName, version

def install():
	pluginName, version = getNameAndVersion()
	fetchPlugin(pluginName, version)

def uninstall():
	pluginName, version = getNameAndVersion()
	removePlugin(pluginName, version)

def installcmd():
	pluginName, version = getNameAndVersion()
	fetchCmdPlugin(pluginName, version)

def uninstallcmd():
	pluginName, version = getNameAndVersion()
	removeCmdPlugin(pluginName, version)

def handleExtraCommand(command, usage):
	if not findCmdPlugin(command):
		print('[CKstyle] CKstyle can not find the subcommand.')
		print('[CKstyle] You can type "ckstyle installcmd %s" to install this command if exists in CKstylePM.' % command)
		return
	cmd = fetchCmdPlugin(command)
	if cmd is None:
		return
	cmd()
