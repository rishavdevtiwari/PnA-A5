# 37. Python program to count the number of even and odd numbers from a series of numbers.  
start=int(input("Enter the beginning of the series : "))
end=int(input("Enter the end of the series : "))
even_count=0
odd_count=0
for i in range(start,end+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"The even count is : {even_count}")
print(f"The odd count is : {odd_count}")