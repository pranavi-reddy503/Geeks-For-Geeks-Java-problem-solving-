#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        for i in range(0,len(arr)):
            for j in range(0,len(arr)-i-1):
                if(arr[j]>arr[j+1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends