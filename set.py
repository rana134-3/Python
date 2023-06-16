#Set is a collection which is unordered and unindexed. No duplicate members. 
s= {45.6,"rage",5,3.5,7+45j,"Hello Python",True,(4.65,"python",8)}
print(type(s))
print(len(s))
s1={1,2,4,3,8,1,2,3,9,8,2,1,"rage","python","rage","python",1,8,2}
print(s1)
l=[1,2,4,3,8,1,2,3,9,8,10,2,1,"rage",10,"hello",9,"rage","hello",1,8,2]
l=list(set(l))
print(l)
s.add("python") #add() method adds an element to the set
print(s)
s.update([5,3.5,"python",10,45.6]) #update() method adds multiple elements to the set
print(s)
s.remove(45.6) #remove() method removes the specified element from the set
print(s)
s.discard("Hello Python") #discard() method removes the specified element from the set
print(s)
s.pop() #pop() method removes the last element from the set
print(s)
s.clear() #clear() method empties the set
print(s)