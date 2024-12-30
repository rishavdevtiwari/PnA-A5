# 44. You have two lists of numbers, and you need to find out which numbers appear in both lists.
lst1=eval(input("Ënter the first list : "))
lst2=eval(input("Enter the second list: "))
for i in lst1:
    if i in lst2:
        print(i,"is common in both lists")
    