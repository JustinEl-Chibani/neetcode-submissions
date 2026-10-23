class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        twon=len(nums)*2
        ans=[0]*twon
        i=0
        while i<len(nums):
            ans[i] = ans[i+len(nums)] = nums[i]
            i+=1
        return ans