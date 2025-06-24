a=[4,5,100,6,2,1]
for i in range(len(a)):
    pos=i
    tem=a[i]
    while pos>0 and a[pos-1]>tem:
        a[pos]=a[pos-1]
        pos=pos-1
    a[pos]=tem
print(a)