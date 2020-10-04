N = int(input())
anos = N // 365
meses = (N % 365) // 30
dias = (N % 365) % 30
print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(anos, meses, dias))
