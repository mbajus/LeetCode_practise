#LeetCode
#189. Rotate Array
# Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums, k) -> None:
        i = len(nums) - 1
        while k != 0:
            nums.insert(0, nums[i])
            nums.pop(i+1)
            k -= 1
        return nums

#checking
print(Solution.rotate2(self = Solution, nums = [1,2,3,4,5,6,7], k = 2))

