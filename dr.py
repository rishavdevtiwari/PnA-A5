# 29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] 
# expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a=["ram","shyam",1,2]
lst=[]
for i in a:
    lst.append('Dr.'+str(i))
print(lst)
