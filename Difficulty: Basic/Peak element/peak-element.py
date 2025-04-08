
class Solution:   
    def peakElement(self, arr):
        # Edge case: If the array is empty
        if not arr:
            return -1  # or raise an exception if needed
        
        n = len(arr)
        
        # If there's only one element, it's trivially the peak
        if n == 1:
            return 0
        
        # Check if the first element is a peak
        if arr[0] > arr[1]:
            return 0
        
        # Check if the last element is a peak
        if arr[n - 1] > arr[n - 2]:
            return n - 1
        
        # Loop through the array to find a peak element in the middle
        for i in range(1, n - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return i
        
        return -1  # If no peak element is found



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends