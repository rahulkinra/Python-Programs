a=[]
for i in range(30):
    a.append(i)
#print(a)
for i in a:
    if i%2==0:
        #print(i)
        if a[i]>a[i-2]:
            b=a[i]
    else:
        if a[i]>a[i-1]:
            c=a[i]
            #print("raja")
print(b)
print(c)

