import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap=[]
    for num in nums:
        pair = (-num, num)
        heapq.heappush(heap, pair)    
    
    result = []
    while heap:
        pair = heapq.heappop(heap)
        original = pair[1]
        result.append(original)
    return result


    #what if i do
    # negate all
    # find max.

    #id need to figure out a way to bring the original numbers back
    # if i make tuples
    # var1=negated , var2=reg
    # this keeps reg, and finds max

    # then for each pair in heap, pop the current min, which is highest number
    # then return 2 value of that tuple



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
