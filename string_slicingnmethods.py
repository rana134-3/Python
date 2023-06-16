#Slicing of string and some of its methods/functions
s="Hello world"
print(s[0:5])
print(s[0::2])
print(s[::-1])
print(s[0:5:-1])
print(s[4:-12:-1])
print(s.count('l')) #count() method returns the number of times the element occurs in the string
print(s.find("o")) #find() method returns the index of the first occurence of the element
print(s.title()) #title() method returns the string in title case
print(s.upper()) #upper() method returns the string in upper case
print(s.lower()) #lower() method returns the string in lower case
print(s.replace("world","Python")) #replace() method replaces the first element with the second element
print(s.casefold()) #casefold() method returns the string in lower case
print(len(s)) #len() method returns the length of the string