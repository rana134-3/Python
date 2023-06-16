#Tuples are immutable and ordered collection of elements enclosed within parentheses. 
t= (45.6,"rage",5,3.5,7,"Hello Python",10,True,[4.65,"python",8])
print(type(t))
print(len(t))
print(t[0:5])
print(t[0::2])
print(t[::-1])
print(t[0:6:-1])
print(t[4:-12:-1])
print(t.count(10)) #count() method returns the number of times the element occurs in the tuple
print(t.index(True)) #index() method returns the index of the first occurence of the element