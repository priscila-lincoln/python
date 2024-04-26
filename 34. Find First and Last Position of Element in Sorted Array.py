class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums)-1
        end = -1
        start =-1

        while low <= high:
            mid = low + (high-low)/2
            if nums[mid] == target:
                end = mid
                low = mid + 1
            elif nums[mid] >= target:
                high = mid -1
            else:
                low = mid+1

        low , high = 0, len(nums)-1

        while low <= high:
            mid = low +(high -low)/2
            if nums[mid]==target:
                start =mid
                high = mid-1
            elif nums[mid]>=target:
                high = mid-1
            else:
                low = mid+1
        return [start,end]
