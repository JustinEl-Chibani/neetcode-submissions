class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, max_count = 0, 0
        for num in nums:
            cnt = cnt + 1 if num else 0
            max_count = max(max_count, cnt)
        return max_count