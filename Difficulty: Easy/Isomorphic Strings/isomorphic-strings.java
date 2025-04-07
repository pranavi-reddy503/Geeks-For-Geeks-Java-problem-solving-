//{ Driver Code Starts
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Arrays;

public class Driver {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        while (tc-- > 0) {
            String s1 = br.readLine();
            String s2 = br.readLine();

            Solution obj = new Solution();

            boolean a = obj.areIsomorphic(s1, s2);
            if (a)
                System.out.println("true");
            else
                System.out.println("false");

            System.out.println("~");
        }
    }
}

// } Driver Code Ends


class Solution {
    // Function to check if two strings are isomorphic.
    public static boolean areIsomorphic(String s1, String s2) {
        // Your code here

        List<Integer> l1 = new ArrayList<>();
        List<Integer> l2 = new ArrayList<>();
        
        // Loop through the first string and store the index of the first occurrence of each character.
        for (char c : s1.toCharArray()) {
            l1.add(s1.indexOf(c));
        }
        
        // Loop through the second string and store the index of the first occurrence of each character.
        for (char c : s2.toCharArray()) {
            l2.add(s2.indexOf(c));
        }
        
        // Compare the two lists.
        if (l1.equals(l2)) {
            return true;
        }
        return false;
    }

   
}