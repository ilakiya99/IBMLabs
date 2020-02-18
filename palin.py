str1 = input("enter a string : ")
str1 = str1.casefold()
str2 = reversed(str1)
if list(str1) == list(str2):
    print("the string is palindrome")
else:
    print("the string is not a palindrome")