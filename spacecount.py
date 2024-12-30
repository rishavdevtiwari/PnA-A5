# 23. Python program to count the space of a given string
str=input("Enter a sentence : ")
count=0
for i in str:
    if i.isspace():
        count+=1
print("Number of spaces in the given string is: ",count)