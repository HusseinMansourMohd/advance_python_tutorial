#Tuples are used to store multiple items in a single variable.
#a collection of Python objects that is ordered and unchangeable.
#immutable doesn't suppot item inserts.
#tuple , ordered , immutable , allows duplicates.

mytuple = ("Max" , 28 , "Boston")
mytuple = ("Max" ,)
tuple ["Max", 28, "Boston"]
print(mytuple)


item = mytuple[2]
"Boston"

item = mytuple[-1]
"Boston "
for x in mytuple:
    print(x)

if "Max" in mytuple:
    print("Yes")

else:
    print("No")

# len = lenght of the tuple

print(len(mytuple))

mytuple = ("p" , 'e' , "l")

#count of a spcific element
print(mytuple.count('p'))
a = [1,2,3,4,5,6,7,8,9]

#slicing  
b = a[2:5]

#steps
b = a[::2]
#reverse list 


name , age , city = mytuple
print(name)
print(age)
print(city)


# reverse tuple
b = a[::-1]


my_tuple = "max", 28 , "Boston"

my_tuple2 = (0, 1, 2, 3 ,4) 

name , age , city = my_tuple

i1, *i2, i3 = my_tuple


print(i1)
print(i2)  # {}
print(i3)

#

import sys
my_List = [0, 1, 2,"hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_List), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit
print(timeit.timeit(stmt ="[0, 1, 2, 3, 4, 5]"), number=1000000) # 0.16

print(timeit.timeit(stmt = "(0 , 1, 3, 4, 5)"), number = 1000000) # 0.019







