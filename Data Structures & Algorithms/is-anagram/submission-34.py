class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictionary = [0]*26
        for i,y in zip(s,t):
            dictionary[ord(i) - ord('a')]+=1
            dictionary[ord(y) - ord('a')]-=1
        return not any(dictionary)