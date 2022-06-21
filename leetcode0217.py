#LeetCode
#217. Contains Duplicate
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        
#checking
print(Solution.containsDuplicate(self = Solution, nums = [1,2,3,1]) == True)
print(Solution.containsDuplicate(self = Solution, nums = [1,2,3,4]) == False)
print(Solution.containsDuplicate(self = Solution, nums = [1,1,1,3,3,4,3,2,4,2]) == True)