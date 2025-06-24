# Binary search
# Array should be ordered
arr = [1,2,3,4]

start_index=0
end_index=len(arr)
k=4
while start_index<end_index:
    mid_index=int((start_index+end_index)/2)
    if arr[mid_index]==k:
        print(mid_index)
        break
    elif arr[mid_index]<k:
        start_index=mid_index
    elif arr[mid_index]>k:
        end_index=mid_index
    