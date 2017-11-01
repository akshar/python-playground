import sys

def wrap(filename,size):
    f = open(filename).readlines()
    for line in f:
        if (len(line) > size):
            print line[:size]
            print line[size:]
        else:
            print line


wrap(sys.argv[1], sys.argv[2])
