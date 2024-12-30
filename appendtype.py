# 33. Write a for loop which appends the type of each element in the first list to the second list.
lst1=eval(input("Enter a list of different types of data types : "))
lst2=[]
for i in lst1:
    lst2.append(type(i))
print(lst2)