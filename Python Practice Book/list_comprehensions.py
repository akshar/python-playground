import sys
pythagorean triplet for num < 25

print [(x,y,z) for x in range(0,25) for y in range(0,25) for z in range(0,25) if( (x ** 2) + (y ** 2) == (z ** 2) ) ]


def uzip(a, b):
    print [(a[i],b[i]) for i in range(len(a))]


uzip([1, 2, 3], ["a", "b", "c"])


def umap(f,cl):
    print [f(x) for x in cl]



def square(x): return x * x
umap(square, range(5))


def ufilter(f,cl):
    print [x for x in cl if f(x)]


def even(x): return x %2 == 0

ufilter(even, range(10))


def uenumerate(l):
    print [(index, l[index]) for index in range(len(l))]


uenumerate(["a", "b", "c"])


def parse_csv(file):
    f = open(file).readlines()
    print [x.split(",") for x in f]


parse_csv(sys.argv[1])
