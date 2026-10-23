class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        rightmax=-1
        for i in range(n-1, -1, -1):
            potentialmax = arr[i]
            arr[i] = rightmax
            rightmax = max(potentialmax,rightmax)
        return arr
        #setting the right most to -1 firstly, then passing to 2nd to right and recursing
        #continuously storing the right most max between y and len(arr) in y-1

#        for i in range(len(arr)-1):
 #           arr[i]=arr[i+1]
  #          for y in range(i+1, len(arr)):
   #             arr[i] = max(arr[y], arr[i])
     #   arr[len(arr) - 1] = -1
    #    return arr
        #test: y=1 c =4 arr[0]=4, y=2 c=5 arr[0]=5 [5,]