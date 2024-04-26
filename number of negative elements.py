#Given a sorted array, find the number of negative elements in it.

new = [-11,-10,-4,-2,-1,2]

nums=[]
for i in range(len(new)):
    if new[i] <0:
        nums.append(0)
    else:
        nums.append(1)
target = 1
low =0
high = len(nums)-1
ans = -1
while low <= high:
    mid = low+ (high-low)//2
    if nums[mid] == target:
        ans = mid
        high = mid-1
    elif nums[mid] <= target:
        low = mid+1
    else:
        high=mid-1
print(ans)
    