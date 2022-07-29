#LeetCode
# 392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s, t) -> bool:
        for l in s:
            if l in t:
                t = t[t.find(l)+1:]
            else:
                return False
        return True

# checks
print(Solution.isSubsequence(self = Solution, s = "abc", t = "ahbgdc"))
print(Solution.isSubsequence(self = Solution, s = "axc", t = "ahbgdc"))
print(Solution.isSubsequence(self = Solution, s = "aaaaaa", t = "bbaaaa"))