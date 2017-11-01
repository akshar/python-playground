import sys

def reverse_line(filename):
    f = open(filename).readlines()
    for x in f:
        print x[::-1]


reverse_line(sys.argv[1])
