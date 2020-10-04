valor = int(input())
val = valor
ntcem = ntcinq = ntvin = ntdez = ntcinco = ntdois = ntum = 0

if val >= 100:
    ntcem = val // 100
    val = val % 100
if val >= 50:
    ntcinq = val // 50
    val = val % 50
if val >= 20:
    ntvin = val // 20
    val = val % 20
if val >= 10:
    ntdez = val // 10
    val = val % 10
if val >= 5:
    ntcinco = val // 5
    val = val % 5
if val >= 2:
    ntdois = val // 2
    val = val % 2
if val >= 1:
    ntum = val // 1

print('{}'.format(valor))
print('{} nota(s) de R$ 100,00'.format(ntcem))
print('{} nota(s) de R$ 50,00'.format(ntcinq))
print('{} nota(s) de R$ 20,00'.format(ntvin))
print('{} nota(s) de R$ 10,00'.format(ntdez))
print('{} nota(s) de R$ 5,00'.format(ntcinco))
print('{} nota(s) de R$ 2,00'.format(ntdois))
print('{} nota(s) de R$ 1,00'.format(ntum))
