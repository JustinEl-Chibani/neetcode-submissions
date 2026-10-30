class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numss= set(nums)
        return len(numss) < len(nums)