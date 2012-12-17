#encoding=utf-8
import sublime, sublime_plugin
import os

class FixstylesafeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        path = os.path.realpath(self.view.file_name()).encode('utf-8')
        cmd = 'fixstyle --safeMode -p "' + path + '"'
        returnValue = os.popen3(cmd)

        returnValue = returnValue[1].read() + returnValue[2].read()

        if returnValue.find('[console.error]') != -1:
            sublime.error_message(returnValue)
        else:
            region = sublime.Region(0, self.view.size())
            self.view.replace(edit, region, returnValue)
            self.view.end_edit(edit)
