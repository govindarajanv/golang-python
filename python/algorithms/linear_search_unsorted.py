def linear_search(arr,target):
    start = 0 
    end = len(arr) - 1 
    
    while start <= end:
        if arr[start] == target:
            return start
        start += 1
    return -1


unsorted_arr = [40,30,20,90,80,60]
ans = linear_search(unsorted_arr,60)
if ans != -1:
    print("Target found at index",ans)
else:
    print("Target not found")