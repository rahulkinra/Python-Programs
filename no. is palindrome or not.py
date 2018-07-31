a=int(input('enter your number'))
b=a
rev=0
while a>0:
    c=a%10;
    #print(c)
    rev=rev*10+c
    #print(rev)
    a=a//10
    #print(a)
if(b==rev):
    print('no. is palindrome')
else:
    print('no. is not palindorme')
    
    
