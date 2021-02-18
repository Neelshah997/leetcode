class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        r = 0
        while(i<n):
            while(j<n):
                ans = s[j:i+1]
                l1 = len(ans)
                l2 = len(set(ans))
                if l1==l2:
                    r = max(r,l1)
                    break
                j+=1
            i+=1
        return r
