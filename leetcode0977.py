#LeetCode
#977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums):
        return sorted([x*x for x in nums])

#checking
print(Solution.sortedSquares(self = Solution, nums = [-7,-3,2,3,11]) == [4,9,9,49,121])