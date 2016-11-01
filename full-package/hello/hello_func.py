import sys


def hello(name="World", stream=None):
    if stream is None:
        stream = sys.stdout
    s = "Hello, %s!\n" % name
    stream.write(s)
