#List is a collection which is ordered and changeable. Allows duplicate members.
l= [1,2,3+9j,4,"Rage",6,7,5,3.5,"Hello Python",10,5]
print(l[-5:-100:-1])
print(l[0:5])
print(l[0::2])
print(l[::-1])
print(l[0:6:-1])
print(l[4:-12:-1])
print(l[0:12])
print(l[-3][0:2])
print(len(l))
l.append("Python") #append() method adds an element at the end of the list
print(l)
l.remove("Rage") #remove() method removes the first occurence of the element
print(l)
l.insert(-4,"Rage") #insert() method inserts an element at the specified index
print(l)
l.insert(5,[1,2,5]) #insert() method inserts an element at the specified index
print(l)
print(l.count(5)) #count() method returns the number of times the element occurs in the list
print(l.index(5)) #index() method returns the index of the first occurence of the element
l.pop(-5) #pop() method removes the element at the specified index
print(l)
l.reverse() #reverse() method reverses the list
print(l)
l.extend("data") #extend() method adds the elements of the iterable to the end of the list
print(l)
l1 = [70,28,-3,0,4,85]
l2 = ["rage","python","data","hello"]
l1.sort() #sort() method sorts the list in ascending order
print(l1)
l2.sort() #sort() method sorts the list in ascending order
print(l2)
l1.sort(reverse=True) #sort() method sorts the list in descending order
print(l1)
l2[0] = "Data Science" #replaces the element at the specified index with the given element
print(l2)
