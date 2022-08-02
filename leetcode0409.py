#LeetCode
# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


class Solution:
    def longestPalindrome1(self, s) -> int:
        count = 0
        i = 0
        while i < len(s):
            print(i, s[i], s)
            if s[i] in s[i+1:]:
                s = s.replace(s[i], "", 2)
                count += 2 
            else:
                i += 1
        if count % 2 == 0 and s != "":
            count += 1
        return count

#checking
print(Solution.longestPalindrome(self = Solution, s = "abccccdd"))
print(Solution.longestPalindrome(self = Solution, s = "abb"))
        