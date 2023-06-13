#Using a while loop, verify if the number A is purely divisible by number B and if so then how many times it can be divisible.
a = int(input("Enter number A: "))
b = int(input("Enter number B: "))

count = 0  # Counter variable to keep track of the number of divisions

while a >= b:
    if a % b == 0:
        a = a // b
        count += 1
    else:
        break

if count > 0:
    print("Number A is divisible by number B ", count, "times.")
else:
    print("Number A is not divisible by number B.")
