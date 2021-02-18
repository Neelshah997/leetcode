class Solution {
    public String longestPalindrome(String s) {
        int ans[][] = new int[s.length()][s.length()];
        int start = 0;
        int maxLength = 1;
        for(int i = 0,j = 0;i<ans.length;i++,j++){
            if (i==j){
                ans[i][j] = 1;
            }
        }
        for (int i = 0; i < s.length() - 1; ++i) {            
            if (s.charAt(i) == s.charAt(i + 1)) {
                    ans[i][i + 1] = 1;
                    start = i;
                    maxLength = 2;
                }
        }
        int n = s.length();
        for (int k = 3; k <= n; ++k) {
 
            for (int i = 0; i < n - k + 1; ++i) {
                int j = i + k - 1;
                   if (ans[i + 1][j - 1] == 1 && s.charAt(i) == s.charAt(j)) {
                    ans[i][j] = 1;

                    if (k > maxLength) {
                        start = i;
                        maxLength = k;
                    }
                }
            }
        }
        return s.substring(start, start + maxLength);   
    }
}