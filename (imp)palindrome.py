# 40. program to check given number is palindrome or not
num = int(input("Enter a number: "))
num_str = str(num)
if num_str == num_str[::-1]:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")