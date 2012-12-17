#encoding=utf-8
import sublime, sublime_plugin
import os

class FixstyleCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        path = os.path.realpath(self.view.file_name().decode('utf-8'))
        cmd = 'fixstyle -p "' + path + '"'
        returnValue = os.popen3(cmd)

        returnValue = returnValue[1].read() + returnValue[2].read()

        if returnValue.find('[console.error]') != -1:
            sublime.error_message(returnValue)
        else:
            region = sublime.Region(0, self.view.size())
            try:
                self.view.replace(edit, region, returnValue.decode('utf-8'))
            except Exception:
                sublime.error_message('not utf-8, wrong file encoding charset');
            self.view.end_edit(edit)
