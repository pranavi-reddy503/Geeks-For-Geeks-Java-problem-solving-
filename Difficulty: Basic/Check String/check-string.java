//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main (String[] args)
    {
        
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            String s = sc.next ();
            if (new Sol().check (s))
                System.out.println ("YES");
            else
                System.out.println ("NO");
        
System.out.println("~");
}
        
    }
}
// Contributed By: Pranay Bansal

// } Driver Code Ends


//User function Template for Java

class Sol
{
    Boolean check (String s)
    {
    if(s.length() <= 1){
        return true;
    }
    char firstchar=s.charAt(0);    
    for(int i=1;i<s.length();i++){
        if(s.charAt(i)!=firstchar){
            return false;
        }
    }
    return true;    // your code here       
    }
}