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

def insertion_sort(a):
    # Pointer is at the second position, all items on the left should be sorted
    # traverse from the pointer to the first position to keep inserting elements to make the sublist sorted
    for i in range(1, len(a)):
        # pointer
        #   j  i
        # 2 7  3  8  5
        pointer = a[i]
        # for traversal in reverse from the pointer till anchor is less than the element encountered
        j = i-1
        while j >=0 and pointer < a[j] :
            print (a)
            a[j+1] = a[j]
            j = j - 1
            #print ("after",a)
        a[j+1] = pointer
    return a

if __name__ == "__main__":
    arr = [40,30,90,20]
    print (insertion_sort(arr))
