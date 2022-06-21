#LeetCode
#3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = count = 0
        word = set()
        for end, letter in enumerate(s):
            if letter in word:
                while s[start] != letter:
                    word.remove(s[start])
                    start += 1
                word.remove(s[start])
                start += 1
            else:
                count = max(count, end - start + 1)
            word.add(letter)
        return count    

#checking
print(Solution.lengthOfLongestSubstring(self = Solution, s = "ibhghhfrrs") == 4)
