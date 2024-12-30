# 22. Python program to calculate the sum of all the even numbers within the given range.
initial=int(input("Enter the starting number : "))
final=int(input("Enter the ending number : "))
sum=0
for i in range(initial,final+1):
    if i%2==0:
        sum+=i
print(f"The sum is {sum}")