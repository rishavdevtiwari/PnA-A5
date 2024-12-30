# 15. Python program that accepts a string and calculate the number of digits and letters and space
s=input("Enter any string: ")
str=0
num=0
space=0
for i in s:
    if i.isdigit():
        num=num+1
    elif i.isalpha():
        str=str+1
    elif i.isspace():
        space=space+1
        
print("Number of digits: ",num)
print("Number of letters: ",str)
print("Number of spaces: ",space)