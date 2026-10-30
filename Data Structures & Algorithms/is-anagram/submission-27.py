class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dicts = defaultdict(int)
        dictt = defaultdict(int)
        for i,y in zip(s,t):
            dicts[i]+=1
            dictt[y]+=1
        return dicts == dictt