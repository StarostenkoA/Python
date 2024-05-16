def SumNum(Num1, Num2):
    if Num1==Num2:
        return Num2
    return Num2 + SumNum(Num1,Num2 - 1);
        
print(SumNum(3,6))

