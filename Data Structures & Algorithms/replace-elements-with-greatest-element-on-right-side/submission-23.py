class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(0, n-1, 1):
            arr[i]=arr[i+1]
            arr[i] = max(arr[i:])
        arr[n-1]=-1
        return arr

#        for i in range(len(arr)-1):
 #           arr[i]=arr[i+1]
  #          for y in range(i+1, len(arr)):
   #             arr[i] = max(arr[y], arr[i])
     #   arr[len(arr) - 1] = -1
    #    return arr
        #test: y=1 c =4 arr[0]=4, y=2 c=5 arr[0]=5 [5,]