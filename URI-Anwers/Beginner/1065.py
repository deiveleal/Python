acum = 0
for i in range(5):
  valr = int(input())
  if valr % 2 == 0:
    acum += 1
print('{} valores pares'.format(acum))
