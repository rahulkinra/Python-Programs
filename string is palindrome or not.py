a_str=input('enter your string')

a_str=a_str.casefold()


re_str=a_str [::-1]
#re_str=a_str
#print(list(rev_str))

if a_str==re_str:
    print("it is palindrome")

else:
    print("it is not palindrome")

