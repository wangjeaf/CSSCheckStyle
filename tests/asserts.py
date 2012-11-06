results = []

def ok(expected, msg = 'ok'):
    results.append([expected, msg])

def equal(expected, actual, msg = 'ok'):
    if expected == actual:
        ok(True, msg)
    else:
        ok(False, msg + '  expect: %s, actual: %s' % (expected, actual))

def notEqual(expected, actual, msg = 'ok'):
    if expected != actual:
        ok(True, msg)
    else:
        ok(False, msg + '   %s is equal to %s' % (expected, actual))

def getResults():
    return results
