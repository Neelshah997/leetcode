class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x<0:
            flag = True
        y = str(abs(x))
        y = y[::-1]
        x = int(y) if flag == False else int(y)*-1
        if x>2**31-1 or x<-2**31:
            return 0
        return x