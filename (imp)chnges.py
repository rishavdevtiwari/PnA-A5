# 11. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
lst=[1,2,3,4]
new_lst=[]
# Inserting "a" at index 1
for i in lst:
    if i == 3:
        continue
    else:
        new_lst.append(i)
new_lst.insert(1,'a')
print(new_lst)