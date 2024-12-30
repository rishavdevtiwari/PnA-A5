# 45. Write a program to determine whether a given number is a prime number.
n=int(input("Enter a number : "))
count=0
for i in range(1,10):
    if n%i==0:
        count+=1
if count>2:
    print(n,"is not a prime number.")
else:
    print(n,"is a prime number.")