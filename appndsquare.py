# 30. Write a for loop which appends the square of each number to the new list.
lst=eval(input("Enter a list of numbers : "))
new_lst=[]
for i in lst:
    if isinstance(i,int):
        new_lst.append(i**2)
print(new_lst)