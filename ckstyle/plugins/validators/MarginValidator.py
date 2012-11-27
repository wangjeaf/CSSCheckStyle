class MarginValidator():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def validate(self):
        realValues = [x for x in self.value.split(' ') if x != '']
        if len(realValues) > 4:
            return False, 'value of margin is too much(items > 4)'
        return True, ''
