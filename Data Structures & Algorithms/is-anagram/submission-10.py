class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a dict which just compares with enumerate
        if len(s) != len(t):
            return False
        ss = defaultdict(int)
        tt = defaultdict(int)
        for i, y in zip(s,t):
            ss[i]+=1
            tt[y]+=1
        return ss == tt