//{ Driver Code Starts
// Initial template for Java

import java.io.*;
import java.util.*;

public class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String s = read.readLine();
            Solution ob = new Solution();

            System.out.println(ob.revStr(s));
        
System.out.println("~");
}
    }
}
// } Driver Code Ends


class Solution {
    static String revStr(String s) {
        StringBuilder sb=new StringBuilder(s); 
        for(int i=0;i<sb.length()/2;i++){
            int front=i;
            int back=sb.length()-1-i;
            char backChar=sb.charAt(back);
            char frontChar=sb.charAt(front);
            sb.setCharAt(front,backChar);
            sb.setCharAt(back,frontChar);
        }
        return sb.toString();
    }
}