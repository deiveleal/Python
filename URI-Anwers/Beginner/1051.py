rendimentos = float(input())
if rendimentos <= 2000.00:
  print('Isento')
elif rendimentos > 2000.00 and rendimentos <= 3000.00:
  print('R$ {:.2f}'.format((rendimentos - 2000.00) * 0.08))
elif rendimentos > 3000.00 and rendimentos <= 4500.00:
  segundaFaixa = rendimentos - 3000.00
  print('R$ {:.2f}'.format((segundaFaixa * 0.18) + (1000 * 0.08)))
else:
  terceiraFaixa = rendimentos - 4500.00
  print('R$ {:.2f}'.format((terceiraFaixa * 0.28) + (1500 * 0.18) + (1000 * 0.08)))
