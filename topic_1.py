
myList = ["bannana", "apple" , "cherry"]

item1 = myList[-1] #print the last element
print(myList)

for i in myList:
    print(i)

if "bana" in myList:
    print("yes")
else:
    print("no")

#append
myList.append("Lemon") 


#pop : return last item and then removes it.

Last_item = myList.pop()

#remove specific element methods 

myList = mylist.remove("apple")

#Delete all items from the list.
myList.clear()

myList = [-3, 1, 4, 5, -6]

myList.sort() # or sorted(myList)

#copy list and slicing:
list_org = [1, 2, 3]
list_cpy = list_org[:]

#Lists: ordered, mutable, allows duplicate elements
myList = [0] * 5
myList2 = [1,2,3,4,5,6]
myList3 = myList + myList2

a = myList[1:5]
a = myList[::1] #from begining to the end use one step

a = myList[::-1] # reverse order a list using only one step at a time

print(a)

###
list_org = ["banna", "cherry", "apple"]

List_cpy = list_org.copy()
List_cpy = list_org[:] # slicing
List_cpy.append("lemon")


print(list_cpy)
print(list_org)

myList = [1, 2 , 3, 4, 5]

b = [i*i for i in myList]

print(myList)
print(b)

