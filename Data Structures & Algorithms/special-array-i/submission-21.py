class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(1, len(nums)-1):
            if nums[i-1] & 1 == nums[i] & 1:
                    return False
        return True