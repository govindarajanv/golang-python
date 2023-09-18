"""
Steps we will follow is
Step 1  Move n-1 disks from source to helper
Step 2  Move nth disk from source to dest
Step 3  Move n-1 disks from helper to dest
"""

def toh(disks,source,target,helper):
    if disks == 1:
        print ("Moving disk 1 from {} to {}".format(source,target))
        return
    toh(disks-1,source,helper,target)
    print("Moving disk {} from {} to {}".format(disks,source,target))
    toh(disks-1,helper,target,source)

if __name__ == "__main__":
    disks = int(input("Number of disks:"))

    toh(disks,'S','H','D')