# 14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
lst=[1,2,3,4,"a","b"]
num_lst=[]
str_lst=[]
for i in lst:
    if isinstance(i,int):
        num_lst.append(i)
    elif isinstance(i,str):
        str_lst.append(i)
    else:
        continue
print(f"Numbers: {num_lst}")
print(f"Strings: {str_lst}")