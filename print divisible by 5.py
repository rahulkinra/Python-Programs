print('enter the value of n');
n1=input();

a=[];
for i in range(0,n1):
    b=int(input('enter the elemte:'))
    a.append(b) #to make a array
for i in range(0,n1):
    if(a[i]%5==0):
        print(a[i]);

