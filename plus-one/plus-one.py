import math
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 0
        s = 0
        digits = digits[::-1]
        for i in range(len(digits)):
            s = digits[i]+carry
            if i == 0:
                s += 1
            
            carry = math.floor(s/10)
            if s>9:
                ans.append(s%10)
            else:
                ans.append(s)
            print(carry,s)
        ans.reverse()
        if carry>0:
            ans.insert(0,carry)
        return ans
