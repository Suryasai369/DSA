a=[1,2,4,5,3]
n=len(a)
for i in range(n):
    low_index=i
    for j in range(i+1,n):
        if a[j]<a[low_index]:
            low_index=j
    if low_index!=i:
        a[low_index],a[i]=a[i],a[low_index]
print(a)