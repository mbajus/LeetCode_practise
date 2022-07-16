#LeetCode
#344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2):
            a = s[i]
            s[i] = s[-i-1]
            s[-i-1] = a
            print(i, s)
        return s

# checks
print(Solution.reverseString(self = Solution, s = ["h","e","l","l","o"]))
print(Solution.reverseString(self = Solution, s = ["H","a","n","n","a","h"]))




