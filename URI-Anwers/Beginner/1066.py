#1066
acumPar = 0
acumImpar = 0
acumPos = 0
acumNeg = 0
for i in range(5):
  valr = int(input())
  if (valr % 2) == 0:
    acumPar += 1
  if (valr % 2) != 0:
    acumImpar += 1
  if valr > 0:
    acumPos += 1
  if valr < 0:
    acumNeg += 1

print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)'
      '\n{} valor(es) negativo(s)'.format(acumPar, acumImpar, acumPos, acumNeg))
