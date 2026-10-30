class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dicts = [0]*26
        dictt = [0]*26
        for i,y in zip(s,t):
            dicts[ord(i) - ord('a')]+=1
            dictt[ord(y) - ord('a')]+=1
        return dicts == dictt