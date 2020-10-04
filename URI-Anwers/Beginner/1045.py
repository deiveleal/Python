# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

#     se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
#     se A**2 = B**2 + C**2, apresente a mensagem: TRIANGULO RETANGULO
#     se A**2 > B**2 + C**2, apresente a mensagem: TRIANGULO OBTUSANGULO
#     se A**2 < B**2 + C**2, apresente a mensagem: TRIANGULO ACUTANGULO
#     se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
#     se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

# Entrada
# A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

# Saída
# Imprima todas as classificações do triângulo especificado na entrada.

''' Resposta aceita no URI. Separado em funções. Uma de ordenação e outra de
comparação dos tipos de triângulo'''

#Função que ordena os valores inseridos
def ordena(num_A, num_B, num_C):
  aux = 0
  #função que ordena uma série de 3 números
  if num_A > num_B and num_A > num_C:
    if num_B < num_C:
      num_B, num_C = num_C, num_B
      return num_A, num_B, num_C
    else:
      return num_A, num_B, num_C
  elif num_B > num_A and num_B > num_C:
    if num_A > num_C:
      num_A, num_B = num_B, num_A
      return num_A, num_B, num_C
    else:
      num_A, num_B, num_C = num_B, num_C, num_A
      return num_A, num_B, num_C
  else:
    if num_A > num_B:
      num_A, num_B, num_C = num_C, num_A, num_B
      return num_A, num_B, num_C
    else:
      num_A, num_C = num_C, num_A
      return num_A, num_B, num_C

#Função que analisa os tipos de triângulos possíveis
def tipos_triangulo(A, B, C):
  if A >= B+C:
    return print('NAO FORMA TRIANGULO')
  if A**2 == B**2+C**2:
    print('TRIANGULO RETANGULO')
  if A**2 > B**2+C**2:
    print('TRIANGULO OBTUSANGULO')
  if A**2 < B**2+C**2:
    print('TRIANGULO ACUTANGULO')
  if A == B and B == C:
    print('TRIANGULO EQUILATERO')
  if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
    print('TRIANGULO ISOSCELES')

A, B, C = input().split(' ')

A = float(A)
B = float(B)
C = float(C)

A, B, C = ordena(A , B, C)

tipos_triangulo(A, B, C)
