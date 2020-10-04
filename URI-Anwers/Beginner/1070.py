base = int(input())
count = 0
while count < 6:
  if (base % 2) != 0:
    print(base)
    count += 1
  base += 1
