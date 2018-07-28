

print('enter the value of n');
n1=input();
print('enter the value of m');
n2=input();

a=[];
c=[];
for i in range(0,n1):
    b=int(input('enter the elemte:'))
    a.append(b) #to make a array
for i in range(0,n2):
    d=int(input('enter the elemte:'))
    c.append(d)

e=[]
e=a+c

f=n1+n2

for i in range(0,f):
    if(f%2==0):
        max=0
        min=e[0]
        for i in e:
            if(i>max):
                max=i;
            if(i<min):
                min=i;

print(max)
print(min)
    
    

#for i in range(0,n1):
#    if(a[i]%5==0):
#        print(a[i]);



#Enter two lists then merge them and after merging if it’s
#even print largest and smallest value in the list and if it’s odd
#then print smallest, middle and the ,largest value.
