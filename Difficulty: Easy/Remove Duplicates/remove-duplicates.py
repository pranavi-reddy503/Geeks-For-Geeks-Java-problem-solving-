#User function Template for python3
class Solution:
	def removeDups(self, str):
        stack = []
        seen = set()
        
        for c in s:
            if c not in seen:
                seen.add(c)
                stack.append(c)
        
        return "".join(stack)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)
        print("~")

# } Driver Code Ends