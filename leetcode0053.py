#LeetCode
#53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

class Solution:
    #1st try, less efficient
    def maxSubArray1(self, nums) -> int:
        count = sum = 0 
        end = len(nums) - 1
        while end != -1:
            if sum + nums[end] > 0:
                sum = sum + nums[end]
                count = max(count, sum)
            else:
                sum = 0
            end -= 1
        if count == 0:
            count = max(nums)
        return count

    #2nd
    def maxSubArray2(self, nums) -> int:
        count = sum = 0 
        for i in nums:
            if sum + i > 0:
                sum = sum + i
                count = max(count, sum)
            else:
                sum = 0
        if count == 0:
            count = max(nums)
        return count        

#checking
print(Solution.maxSubArray1(self = Solution, nums = [-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(Solution.maxSubArray2(self = Solution, nums = [-2,1,-3,4,-1,2,1,-5,4]) == 6)
        