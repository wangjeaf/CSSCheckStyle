#encoding=utf-8
import sublime, sublime_plugin
import os

class CkstyleCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        path = os.path.realpath(self.view.file_name().decode('utf-8'))
        if os.path.splitext(path)[1] != '.css':
            sublime.error_message('Not a CSS file!')
            return
            
        cmd = 'ckstyle "' + path + '"'
        os.popen3(cmd)
        resultFile = self.view.file_name() + '.ckstyle.txt'
        if os.path.exists(resultFile):
            self.view.window().open_file(self.view.file_name() + '.ckstyle.txt')
        else: 
            sublime.message_dialog('No mistake found in this CSS, NB!')
