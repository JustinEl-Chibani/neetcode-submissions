class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a dict which just compares with enumerate
        if len(s) != len(t):
            return False
        dictt = defaultdict(int)
        dicttt = defaultdict(int)
        for ss, tt in zip(s,t):
            dictt[ss] += 1
            dicttt[tt] += 1
        return dictt == dicttt