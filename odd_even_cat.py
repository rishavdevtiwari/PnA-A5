# 12. Given list is [1,2,3,4,5] separate the elements into odd and even categories.
lst=[1,2,3,4,5]
odd_lst=[]
even_lst=[]
for i in lst:
    if i%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print("EVEN: ",even_lst)
print("ODD:",odd_lst)

