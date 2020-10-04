range_de_teste = int(input())
for i in range(range_de_teste):
  caso_teste = int(input())
  if caso_teste == 0:
    print('NULL')
  elif caso_teste % 2 == 0:
    if caso_teste < 0:
      print('EVEN NEGATIVE')
    else:
      print('EVEN POSITIVE')
  else:
    if caso_teste < 0:
      print('ODD NEGATIVE')
    else:
      print('ODD POSITIVE')
