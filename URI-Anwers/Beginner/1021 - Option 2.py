N = float(input())
val = int(N*100)

ntCem = val / 10000
val = val % 10000
ntCinq = val / 5000
val = val % 5000
ntVin = val / 2000
val = val % 2000
ntDez = val / 1000
val = val % 1000
ntCinco = val / 500
val = val % 500
ntDois = val / 200
val = val % 200
mdUm = val / 100
val = val % 100
mdCinq = val / 50
val = val % 50
mdVin = val / 25
val = val % 25
mdDez = val / 10
val = val % 10
mdCinco = val / 5
val = val % 5
mdUmCent = val / 1

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % ntCem)
print("%d nota(s) de R$ 50.00" % ntCinq)
print("%d nota(s) de R$ 20.00" % ntVin)
print("%d nota(s) de R$ 10.00" % ntDez)
print("%d nota(s) de R$ 5.00" % ntCinco)
print("%d nota(s) de R$ 2.00" % ntDois)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % mdUm)
print("%d moeda(s) de R$ 0.50" % mdCinq)
print("%d moeda(s) de R$ 0.25" % mdVin)
print("%d moeda(s) de R$ 0.10" % mdDez)
print("%d moeda(s) de R$ 0.05" % mdCinco)
print("%d moeda(s) de R$ 0.01" % mdUmCent)
