#create a list containing 25 int values. Using for loop and if-else condition print if the element is divisible by 3 or not.
l= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in l:
    if i%3==0:
        print(i,"is divisible by 3")
    else:
        print(i,"is not divisible by 3")