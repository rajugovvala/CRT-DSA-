#binary search
num=[1,23,44,55,66,899]
target=66
nums=sorted(num)
left=0
right=len(nums)-1
flag=-1

while left <= right:
    mid=(left+right)//2
    if num[mid]==target:
        flag=mid
        break
    elif num[mid]>target:
        mid=mid-1
    else:
        left=mid+1
if flag==-1:
    print("target not found")
else:
    print("target found at index:",flag)
