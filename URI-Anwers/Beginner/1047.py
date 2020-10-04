entradaHorasMinutos = input()
hrInicial, minInicial, hrFinal, minFinal = entradaHorasMinutos.split(' ')
hrInicial, minInicial, hrFinal, minFinal = int(hrInicial)*60, int(minInicial), int(hrFinal)*60, int(minFinal)
tempoInicial = hrInicial + minInicial
tempoFinal = hrFinal + minFinal

if tempoInicial == tempoFinal:
  print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif tempoInicial <= tempoFinal:
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format((
      tempoFinal - tempoInicial) // 60, (tempoFinal - tempoInicial) % 60))
else:
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(((tempoFinal - tempoInicial)
   + 1440) // 60, ((tempoFinal - tempoInicial)+1440) % 60))
