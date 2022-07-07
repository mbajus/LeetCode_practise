class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        i = nums.count(0)
        while i != 0:
            nums.remove(0)
            nums.append(0)
            i -= 1