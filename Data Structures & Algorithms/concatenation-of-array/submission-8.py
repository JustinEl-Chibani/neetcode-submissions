class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        twon=len(nums)*2
        ans=[0]*twon
        for i in range(len(nums)):
            ans[i] = nums[i]
        for y in range(len(nums),twon):
            ans[y] = nums[y-len(nums)]
        return ans