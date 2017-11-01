f = open("foobar.txt")
# realine will return '' when there is no data
print f.readline()
print f.readline()
print f.readline()
print f.readline()

f.close()
# write is used to write to file in write or append mode

f = open("foobar.txt", 'a')
f.write("random foo")
f.close()
f = open("foobar.txt")
print f.read()
f.close()

# The writelines method is convenient to use when the data is available as a list of lines.

f = open("foobar.txt",'a')
f.writelines(['a\n', 'b\n', 'c\n'])
f.close()
