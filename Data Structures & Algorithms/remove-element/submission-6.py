class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #in place no copy
        # return num in nums not equal to val, so k
        #i cant use array functions i think
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k]=nums[i]
                k+=1 # this is false since if back to back val im cooked
        return k