def binary_search(arr,target):
    start = 0 
    end = len(arr) - 1 
    
    while start <= end:
        mid = (start + end)//2 
        
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid

    return -1


arr = [20,30,40,60,80,90]
ans = binary_search(arr,60)
if ans != -1:
    print("Target found at index",ans)
else:
    print("Target not found")