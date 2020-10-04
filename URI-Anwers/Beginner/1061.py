dia = input().split(' ')
diaIni = int(dia[1]) * 86400
hrIni, minIni, segIni = input().split(':')

dia = input().split(' ')
diaFin = int(dia[1]) * 86400
hrFin, minFin, segFin = input().split(':')

hrIniTot = (int(hrIni) * 3600) + (int(minIni) * 60)+ (int(segIni))
hrFinTot = (int(hrFin) * 3600) + (int(minFin) * 60) + (int(segFin))

W = int(((diaFin + hrFinTot) - (diaIni + hrIniTot)) / 86400)
restoDeW = int(((diaFin + hrFinTot) - (diaIni + hrIniTot)) % 86400)
X = int(restoDeW / 3600)
restoDeX = int(restoDeW % 3600)
Y = int(restoDeX / 60)
Z = int(restoDeX % 60)

print('{0} dia(s)\n{1} hora(s)\n{2} minuto(s)\n{3} segundo(s)'.format(W, X, Y, Z))
