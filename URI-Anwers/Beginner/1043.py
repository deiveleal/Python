A ,B ,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

if (A < (B+C)) and (B < (A+C)) and (C < (A+C)):
    Perimetro = A+B+C
    print("Perimetro = %1.1f" %(Perimetro))
else:
    Area = ((A+B)*C)/2
    print("Area = %1.1f" %(Area))
