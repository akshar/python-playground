def noob_extsort(col):
    for index,item in enumerate(col):
        col[index] = item.split(".")
    col.sort(key=lambda x: x[1])
    for index,item in enumerate(col):
        col[index] = item[0]+"."+item[1]
    print col



noob_extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    # ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
