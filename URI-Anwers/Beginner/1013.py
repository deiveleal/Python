VALENTRADA=input().split(' ')

A=int(VALENTRADA[0])
B=int(VALENTRADA[1])
C=int(VALENTRADA[2])

MAB=(A+B+abs(A-B))/2
MABC=(MAB+C+abs(MAB-C))/2

print('%d eh o maior' %MABC)
