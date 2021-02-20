import functools 
  
class Solution:
    def fractionAddition(self, expression: str) -> str:
        sign = 1
        n = len(expression)
        div = False
        numerator = []
        denominator = []
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