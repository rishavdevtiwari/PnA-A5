# 41. program to check given number is armstrong or not
str_num=input("Enter a number : ")
num=int(str_num)
sum=0
for i in range(len(str_num)):
    digit=int(str_num[i])
    sum+=digit**3
if num==sum:
        print(num,"is an armstrong number")
else:
        print(num,"is not an armstrong number")