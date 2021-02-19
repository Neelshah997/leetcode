class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        i = 0 
        while(i<32):
            lsb = n&1
            reverselsb = lsb<<31-i
            result = result|reverselsb
            n = n>>1
            i+=1
        return result