def tempo_duracao(hr_inicial, hr_final):
  if hr_inicial == hr_final:
    return print('O JOGO DUROU 24 HORA(S)')
  elif hr_inicial > hr_final and (hr_inicial-hr_final)>1:
    return print('O JOGO DUROU',24-(hr_inicial - hr_final), 'HORA(S)')
  else:
    return print('O JOGO DUROU',hr_final - hr_inicial,'HORA(S)')

hr = input()
hr_inicial, hr_final = hr.split(' ')
hr_inicial = int(hr_inicial)
hr_final = int(hr_final)

tempo_duracao(hr_inicial, hr_final)
