# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou 
#"Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.
# Entrada
# A entrada contém valores inteiros.
# Saída
# A saída deve conter uma das mensagens conforme descrito acima.

A, B = input().split(' ')

A = int(A)
B = int(B)
C = max(A,B)
B = min(A,B)
A = C

if A % B == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
