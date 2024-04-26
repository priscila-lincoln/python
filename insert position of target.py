def searchInsert( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums)-1

    if target> nums[high]:
        return high

    while(low<=high):
        mid = low + (high-low)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]< target:
            low = mid+1
        elif nums[mid]> target and nums[mid-1]<target:
            return mid
        else:
            high = mid-1

array = [1,3,5,11,12,56]
t = 14
print(searchInsert(array,t))
       