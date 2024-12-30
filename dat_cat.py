# 13. Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types
lst=[1,2,3,"d",4,5,"a"]
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