#LeetCode
#383. Ransom Note
#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if magazine.find(i) >= 0:
                magazine = magazine[:magazine.find(i)] + magazine[magazine.find(i)+1:]
            else:
                return False
        return True