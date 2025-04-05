#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return ""
        arr.sort()
        first,last=arr[0],arr[-1]
        prefix=[]
        for i in range (min(len(first),len(last))):
            if(first[i]==last[i]):
                prefix.append(first[i])
            else:
                break
        return"".join(prefix)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        ans = ob.longestCommonPrefix(arr)

        if not ans:
            print("\"\"")
        else:
            print(ans)

# } Driver Code Ends