class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #in place no copy
        # return num in nums not equal to val, so k
        #i cant use array functions i think
        i,n = 0, len(nums)
        while i<n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n-=1
            else: i+=1
        return n