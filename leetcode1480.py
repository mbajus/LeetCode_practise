#LeetCode
#1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums):
        i = 1
        while i != len(nums):
            nums[i] = nums[i] + nums[i-1]
            i += 1
        return nums


# checks
print(Solution.runningSum(self = Solution, nums = [1,2,3,4]))
print(Solution.runningSum(self = Solution, nums = [3,1,2,10,1]))




