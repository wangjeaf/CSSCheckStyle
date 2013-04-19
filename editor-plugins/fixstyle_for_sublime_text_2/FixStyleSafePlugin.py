#encoding=utf-8
import sublime, sublime_plugin
import os
from helper import getCkstylePath

class FixstylesafeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        path = os.path.realpath(self.view.file_name()).decode('utf-8')
        if os.path.splitext(path)[1] != '.css':
            sublime.error_message('Not a CSS file!')
            return
            
        cmd = getCkstylePath() + ' fix --safeMode -p "' + path + '"'
        returnValue = os.popen3(cmd)

        returnValue = returnValue[1].read() + returnValue[2].read()

        if returnValue.find('[console.error]') != -1:
            sublime.error_message(returnValue)
        else:
            region = sublime.Region(0, self.view.size())
            msg = self.getRealMsg(returnValue)
            try:
                self.view.replace(edit, region, msg)
            except Exception:
                sublime.error_message('ERROR, maybe because file encoding charset is not utf-8');
            self.view.end_edit(edit)

    def getRealMsg(self, msg):
        for charset in ['utf-8', 'gbk', 'gb2312']:
            try:
                msg.decode(charset)
                return msg.decode(charset)
            except Exception:
                pass
        return msg
