inic = int(input())
fin = int(input())
if inic > fin:
  fin, inic = inic, fin
acum = 0
i = inic + 1
while i < fin:
  if (i % 2) != 0:
    acum += i
  i = i + 1
print(acum)
