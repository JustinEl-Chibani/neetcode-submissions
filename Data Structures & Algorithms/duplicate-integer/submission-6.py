class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt = defaultdict(int)
        for num in nums:
            dictt[num] += 1
            if dictt[num]==2:
                return True
        return False