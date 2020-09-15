import sys

def test():
    for line in sys.stdin():
        yield line.read()


a = test()

for i in a:
    print(i)
