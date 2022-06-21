#LeetCode
#704. Binary Search
#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums, target) -> int:
        low = 0
        max = len(nums)-1
        while True:
            mid = round((low+max)/2)
            if nums[mid] > target:
                max = mid -1
            elif nums[mid] < target:
                low = mid +1
            if nums[mid] == target:
                return mid
            elif low > max:
                return -1

#checking
print(Solution.search(self = Solution, nums = [-1,0,3,5,9,12], target = 9) == 4)
print(Solution.search(self = Solution, nums = [-1,0,3,5,9,12], target = 2) == -1)
print(Solution.search(self = Solution, nums = [5], target = -4) == -1)
print(Solution.search(self = Solution, nums = [2,5], target = 5) == 1)