qtd_test = int(input())
incount = 0
outcount = 0
for i in range(qtd_test):
  entrada = int(input())
  if entrada >= 10 and entrada <= 20:
    incount += 1
  else:
    outcount += 1
print('{} in\n{} out'.format(incount, outcount))
