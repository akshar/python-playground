def wordcount(filename):
    print len(open(filename).read().split())

def linecount(filename):
    print len(open(filename).readlines())


wordcount("foobar.txt")
linecount("foobar.txt")
