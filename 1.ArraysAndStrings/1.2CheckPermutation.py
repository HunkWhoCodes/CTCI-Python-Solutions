# https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy

# Complexity: Time: O(n) and Space: O(n) (Generic Case for all Unicode chars)
# Total possible unicode chars can be 1.1 Million: https://stackoverflow.com/questions/5924105/how-many-characters-can-be-mapped-with-unicode/5928054#5928054

# O(1) space solution with 26 length array and no hash table
# Applicable if strings only have lowercase alphabet letters

# Anagram vs Permutation: Ideally anagram has some meaning but permutation does not. But the LC question does not specify that.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = [0] * 26
        
        for char in s:
            diff = ord(char) - ord("a")
            mapping[diff] += 1
        
        # print(mapping)
        
        for char in t:
            diff = ord(char) - ord("a")
            mapping[diff] -= 1
        
        for count in mapping:
            if count > 0:
                return False
        
        return True
                                  
        
# This is generic O(n) time and O(n) space solution applicable for Unicode characters too (not just alphabets)

# Using only 1 hash table: Make a counter from one string and then iterate through another
# If the char not in the hash table, return False else reduce the count of the char in hash table
# Again iterate through hash table, if any element has value more than 0 then return false 
# else out of loop return True
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCount = Counter(s)
        
        for c in t:
            if c not in t:
                return False
            else:
                sCount[c] -= 1
        
        for i in sCount:
            if sCount[i] != 0:
                return False
        
        return True
"""            
        
        
# With two hash tables:
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCount = Counter(s)
        tCount = Counter(t)
        for key, val in sCount.items():
            if key not in tCount:
                return False
            else:
                if val != tCount[key]:
                    return False
                else:
                    continue
        
        return True
'''
