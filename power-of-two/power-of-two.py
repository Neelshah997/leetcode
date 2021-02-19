class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        flag = False
        if n<0:
            return False
        for i in bin(n)[2:]:
            if int(i) ==1 and flag == True:
                return False
            elif int(i)==1 and flag == False:
                flag = True
        if flag == False:
            return False
        return True
