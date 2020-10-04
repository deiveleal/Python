VALENTRADA=input().split(' ')

A=float(VALENTRADA[0])
B=float(VALENTRADA[1])
C=float(VALENTRADA[2])

print('TRIANGULO: {:.3f}'.format((A*C)/2))
print('CIRCULO: {:.3f}'.format((C**2)*3.14159))
print('TRAPEZIO: {:.3f}'.format(((A+B)*C)/2))
print('QUADRADO: {:.3f}'.format(B*B))
print('RETANGULO: {:.3f}'.format(A*B))
