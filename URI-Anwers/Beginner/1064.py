#1064
sumVar = 0
mediumVar = 0
for i in range(6):
  enterVar = float(input())
  if enterVar > 0:
    sumVar += 1;
    mediumVar += enterVar
print('{} valores positivos\n{:.1f}'.format(sumVar,mediumVar/sumVar))
