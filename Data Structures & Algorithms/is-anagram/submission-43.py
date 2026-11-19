class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictionaryI =[0]*26
        dictionaryY = [0]*26
        for i,y in zip(s,t):
            dictionaryI[ord(i)-ord('a')] += 1
            dictionaryI[ord(y)-ord('a')] -= 1
        return not any(dictionaryI)









#        dictionary = [0]*26
 #       for i,y in zip(s,t):
  #          dictionary[ord(i) - ord('a')]+=1
   #         dictionary[ord(y) - ord('a')]-=1
    #    return not any(dictionary)