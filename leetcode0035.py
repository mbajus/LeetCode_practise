#LeetCode
#35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums, target) -> int:
        low = 0
        max = len(nums)
        while True:
            if low >= max:
                return low
            mid = (low+max)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                max = mid
            elif nums[mid] < target:
                low = mid +1

#checking
print(Solution.searchInsert(self = Solution, nums = [1,3,5,6], target = 5) == 2)
print(Solution.searchInsert(self = Solution, nums = [1,3,5,6], target = 2) == 1)
print(Solution.searchInsert(self = Solution, nums = [1,3,5,6], target = 7) == 4)
print(Solution.searchInsert(self = Solution, nums = [6], target = 1) == 0)
print(Solution.searchInsert(self = Solution, nums = [6], target = 6) == 0)
print(Solution.searchInsert(self = Solution, nums = [6], target = 7) == 1)
print(Solution.searchInsert(self = Solution, nums = [6,10], target = 11) == 2)
