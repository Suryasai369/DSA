arr = [3,2,1,5,4]
unsorted_until_index=len(arr)-1
isSorted=False
while not isSorted:
    isSorted=True
    for i in range(unsorted_until_index):
        if arr[i]>arr[i+1]:
            isSorted=False
            arr[i],arr[i+1]=arr[i+1],arr[i]
    unsorted_until_index-=1
print(arr)