class Cleaner():
    @staticmethod
    def clearName(name):
        name = name.strip()
        if name.startswith('_') or name.startswith('*') or name.startswith('+'):
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
        return comment.strip()
