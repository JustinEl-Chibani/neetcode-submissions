class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(len(nums)):
           # for j in range(i+1, len(nums)):
          #      if nums[i]+nums[j] == target:
         #           return [i,j]
        #return []


        #init dict
        ##add key,value pair to dict
        #where the key = value
        #        value = index
        #enumerate nums. o(n) calculate the difference need to get to target
        #see if target is in dictionary o(1) and is different then 
        # first number, so diff index
        #if so return indices of both

        dictionary = {}
        for index,value in enumerate(nums):
            dictionary[value] = index
        
        for i,n in enumerate(nums):
            diff = target-n
            if diff in dictionary and dictionary[diff]!=i:
                return [i, dictionary[diff]]     
        return []
