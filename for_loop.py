for i in range(1,10):
    if i%5 != 0:
        print(i)

av = 5
x = int(input("how many candy u want"))
i = 1
while i<=x:
    if i>av:
        print("out of stock")
        break
    print("candy")
    i+=1
print("bye")

for i in range (1,101):
    if i%2!=0:
        pass
    else:
        print(i)

print("bye")

for i in range (1,101):
    if i%3 == 0 or i%5 == 0:
        continue
    print(i)
print("bye")

for i in range (4):
    for j in range (i+1):
        print("# ",end="")
    print()

for i in range (4):
    for j in range (4-i):
        print("# ",end="")
    print()

y = int(input("enter a number"))
for i in range (2,y):
    if y % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# To take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")
