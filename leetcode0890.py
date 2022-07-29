#LeetCode
# 890. Find and Replace Pattern
# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

class Solution:
    def findAndReplacePattern(self, words, pattern):
        n = 0
        while n != len(words):
            i = 1
            while i != len(words[n]):
                if words[n][i] == words[n][pattern.find(pattern[i])] and pattern[i] == pattern[words[n].find(words[n][i])]:
                    i += 1
                else:
                    print(words[n])
                    words.pop(n)
                    n -= 1
                    break
            n += 1            
        return words
       

# checks
print(Solution.findAndReplacePattern(self = Solution, words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))
