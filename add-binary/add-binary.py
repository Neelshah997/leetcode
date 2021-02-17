class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        l1 = len(a)
        l2 = len(b)
        b = b[::-1]
        l = min(l1,l2)
        ans = ""
        carry = 0
        i = 0
        for i in range(l):
            s = int(a[i])+int(b[i])+carry
            carry = 0 
            if s>1:
                carry = 1
            ans+=str(s%2)
            print(carry,s)
        i = l
        while(i<l1):
            s = int(a[i])+carry
            carry = 0
            if s>1:
                carry = 1
            ans+=str(s%2)
            i+=1
        while(i<l2):
            s = int(b[i])+carry
            carry = 0
            if s>1:
                carry = 1
            ans+=str(s%2)
            i+=1
        if carry>0:
            ans+=str(carry)
        print(ans[::-1])
        return ans[::-1]