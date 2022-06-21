#LeetCode
#1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target):
        for i, a in enumerate(nums):
            if ((target - a) in nums) and nums.index(target - a) != i:
                return [i, nums.index(target - a)]

#checking
print(Solution.twoSum(self = Solution, nums = [1,6142,8192,10239], target = 18431))        
print(Solution.twoSum(self = Solution, nums = [2,7,11,15], target = 9))   
print(Solution.twoSum(self = Solution, nums = [3,2,4], target = 6))   
print(Solution.twoSum(self = Solution, nums = [3,3], target = 6))    
