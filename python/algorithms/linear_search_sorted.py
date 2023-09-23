def linear_search(arr,target):
    start = 0 
    end = len(arr) - 1 
    
    while start <= end:
        if arr[start] == target:
            return start
        elif arr[start] > target:
            break
        start += 1
    return -1


sorted_arr = [20,30,40,60,80,90]
ans = linear_search(sorted_arr,60)
if ans != -1:
    print("Target found at index",ans)
else:
    print("Target not found")