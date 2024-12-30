# 42. Write a for loop that removes all vowels (a, e, i, o, u) from a string.
vowels=['a','e','i','o','u']
str=input("Enter a string : ")
for i in str:
    if i in vowels:
        str=str.replace(i,'')
print(str)