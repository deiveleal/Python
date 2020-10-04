range_entrada = int(input())
for i in range(range_entrada + 1):
  if i == 0:
    pass
  elif i % 2 == 0:
    print('{}^2 = {}'.format(i, i ** 2))
