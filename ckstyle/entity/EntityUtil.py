from ckstyle.browsers.BinaryRule import ALL

import re
replacer1 = re.compile('\s*{\s*')
replacer2 = re.compile('\s*:\s*')
replacer3 = re.compile('\s*;\s*}\s*')
replacer4 = re.compile('\s*;\s*')
replacer5 = re.compile('\s\s+')
replacer6 = re.compile('\(\s+')
replacer7 = re.compile('\s+\)')
replacer8 = re.compile('\s+,')
replacer9 = re.compile(',\s+')

class Cleaner():
    @staticmethod
    def clean(msg):
        msg = msg.strip().replace('\r', '').replace('\n', '').replace(' ' * 4, ' ')
        msg = replacer1.sub('{', msg)
        msg = replacer2.sub(':', msg)
        msg = replacer3.sub('}', msg)
        msg = replacer4.sub(';', msg)
        msg = replacer5.sub(' ', msg)
        msg = replacer6.sub('(', msg)
        msg = replacer7.sub(')', msg)
        msg = replacer8.sub(',', msg)
        msg = replacer9.sub(',', msg)
        msg = msg.strip()
        return msg

    @staticmethod
    def clearName(name):
        name = name.strip()
        # #padding: 10px???
        if name.startswith('_') or name.startswith('*') or name.startswith('+') or name.startswith('#'):
            name = name[1:]
        if name.startswith('-'):
            if name.startswith('-moz-') or name.startswith('-webkit-') or name.startswith('-ms-') or name.startswith('-o-') or name.startswith('-khtml-'):
                name = '-'.join(name.split('-')[2:])
        return name.lower()

    @staticmethod
    def clearValue(value):
        value = value.strip()
        if value.endswith(';'):
            value = value[0: - 1]
        return value

    @staticmethod
    def clearValues(values):
        values = values.strip()
        return values

    @staticmethod
    def clearSelector(selector):
        return ' '.join(selector.split('\n')).strip()

    @staticmethod
    def clearComment(comment):
        comment = comment.strip()
        if len(comment) != 0 and comment.find('\n') == -1:
            comment = comment.replace('/*', '').replace('*/', '').strip()
            comment = '/* ' + comment + ' */'
        return comment
