class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        ct = 0
        while(i<32):
            if n&1==1:
                ct+=1            
            n = n>>1
            i+=1
        return ct