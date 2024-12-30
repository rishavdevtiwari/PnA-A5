# 39. Write a for loop to find the sum of even and odd numbers separately in a range from 1 to 100.
evensum=0
oddsum=0
for i in range(1,101):
    if i%2==0:
        evensum+=i
    else:
        oddsum+=i
print(f"Sum of even numbers = {evensum}")
print(f"Sum of odd numbers = {oddsum}")