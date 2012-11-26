def containsHack(name, strippedName, value):
    return name != strippedName or value.find('\9') != -1
