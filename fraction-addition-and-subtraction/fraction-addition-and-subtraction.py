import functools 
  
class Solution:
    def fractionAddition(self, expression: str) -> str:
        sign = 1
        n = len(expression)
        numerator = []
        denominator = []
        def find_gcd(x, y): 
            while(y): 
                x, y = y, x % y 
            return x 
        prev = 0
        gcd = 1
        index = -1
        div = False
        val = ""
        for i in range(n):
            if expression[i] == "-":
                sign = -1
                if div == True:
                    denominator.append(int(val))
                    val = ""
            elif expression[i] =="+":
                sign = 1
                if div == True:
                    denominator.append(int(val))
                    val =""
            elif expression[i] == "/":
                numerator.append(int(val)*sign)
                val = ""
                div = True
            else:
                val+=expression[i]
            print(val)
        denominator.append(int(val))
        x=0
        y=1
        for i in range(len(numerator)):
            x=x*denominator[i]+y*numerator[i]
            y*=denominator[i]
            gc=math.gcd(x,y)
            x//=gc
            y//=gc
        return str(x)+"/"+str(y)