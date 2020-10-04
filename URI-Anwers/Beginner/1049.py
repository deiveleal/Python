vertebradoInvertebrado = input()
avemamifinsetanel = input()
alimentanimal = input()

if vertebradoInvertebrado == 'vertebrado':
  if avemamifinsetanel == 'ave':
    if alimentanimal == 'carnivoro':
      print('aguia')
    else:
      print('pomba')
  else:
    if alimentanimal == 'onivoro':
      print('homem')
    else:
      print('vaca')

else:
  if avemamifinsetanel == 'inseto':
    if alimentanimal == 'hematofago':
      print('pulga')
    else:
      print('lagarta')
  else:
    if alimentanimal == 'hematofago':
      print('sanguessuga')
    else:
      print('minhoca')
