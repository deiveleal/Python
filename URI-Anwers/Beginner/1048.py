sal = float(input())
if sal <= 400.00:
  print("Novo salario: {:.2f}".format(sal+sal*0.15))
  print("Reajuste ganho: {:.2f}".format(sal*0.15))
  print("Em percentual: 15 %")
elif sal > 400.00 and sal <= 800.00:
  print("Novo salario: {:.2f}".format(sal+sal*0.12))
  print("Reajuste ganho: {:.2f}".format(sal*0.12))
  print("Em percentual: 12 %")
elif sal > 800.00 and sal <= 1200.00:
  print("Novo salario: {:.2f}".format(sal+sal*0.10))
  print("Reajuste ganho: {:.2f}".format(sal*0.10))
  print("Em percentual: 10 %")
elif sal > 1200.00 and sal <= 2000.00:
  print("Novo salario: {:.2f}".format(sal+sal*0.07))
  print("Reajuste ganho: {:.2f}".format(sal*0.07))
  print("Em percentual: 7 %")
else:
  print("Novo salario: {:.2f}".format(sal+sal*0.04))
  print("Reajuste ganho: {:.2f}".format(sal*0.04))
  print("Em percentual: 4 %")
