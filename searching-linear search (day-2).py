nums=[12,332,43,546,6,5]
target=332
flag=-1
n=len(nums)
for index in range(n):
    if nums[index]==target:
        flag=index
        break
if flag==-1:
    print("not found")
else:
    print("target found at:",flag)
