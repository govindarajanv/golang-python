"""
[40, 30, 90, 20]
40 <--> 30
[30, 40, 90, 20]
No Change as 40 < 90
[30, 40, 90, 20]
90 <--> 20
[30, 40, 20, 90]
No Change as 30 < 40
[30, 40, 20, 90]
40 <--> 20
[30, 20, 40, 90]
30 <--> 20
[20, 30, 40, 90]
"""

def bubble_sort(arr):
    n = len(arr)
    print (arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                print (arr[j],"<-->",arr[j+1])
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
            else:
                print ("No Change as",arr[j],"<",arr[j+1])
            print (arr)

        
if __name__ == "__main__":
    arr = [40,30,90,20]
    bubble_sort(arr)