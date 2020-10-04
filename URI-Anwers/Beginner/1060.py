vals = [float(input()) for num in range(0,6)]
contaPos = 0
for num in range(len(vals)):
  if vals[num] > 0:
    contaPos += 1
print('{} valores positivos'.format(contaPos))
