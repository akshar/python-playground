import sys

def grep(filename,search_term):
    f = open(filename).readlines()
    for line in f:
        if (search_term in line):
            print line


grep(sys.argv[1], sys.argv[2])
