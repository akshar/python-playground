age = input("enter your age")
new_age = int(age) + 50;
print(new_age)


k =1;

for x in range(1,11):
    k=k * x

print(k)


def factorial(x):
    if x == 1:
        return 1;
    else:
        return x * factorial(x-1)


print(factorial(5))



def reverse(l):
    return l[::-1]

reverse(range(0,5))
reverse(reverse(range(0,5)))
[0, 1, 2, 3, 4]


def cumulative_sum(l):
    print l
    for index,item in enumerate(l):
        if index == 0:
            l[index] = item
        else:
            l[index] = l[index-1] + l[index]

    return l


print cumulative_sum(range(1,5))



def cumulative_product(lol):
	print lol
	for index,item in enumerate(lol):
		if index ==0:
			lol[index] = item
		else:
			lol[index] = lol[index-1] * lol[index]

	return lol

print cumulative_product(range(1,10))



ans=[]
def group(l,size):
	if(len(l) == 0):
		print ans
	else:
		ans.append(l[0:size])
		group(l[size:],size)


print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
# print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)


def unq_list(l):
    x = []
    for k in l:
        if not (k in x):
            x.append(k)

    print x



def lensort(l):
	print l.sort(key= len)


lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])




def unique2(l,f):
    x= []
    for k in l:
	if not(f(k) in x):
	    x.append(k)

print x


unique2(["python", "Clojure", "Python", "clojure"], lambda s: s.lower())
