import sys

def reverse_file(filename):
    f = open(filename).readlines()
    f = f[::-1]
    for x in f:
        print x


reverse_file(sys.argv[1])
