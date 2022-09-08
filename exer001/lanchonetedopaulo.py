subtotal = 0 #acumulador
print('Bem vindo a Lanchonete do Paulo Vinicius Sales Moura')
print('********************Cardápio********************')
print('| Código |        Descrição      | Valor |')
print('|  100   |    Cachorro-Quente    |  9,00 |')
print('|  101   | Cachorro Quente Duplo | 11,00 |')
print('|  102   |         X-Egg         | 12,00 |')
print('|  103   |        X-Salada       | 13,00 |')
print('|  104   |        X-Bacon        | 14,00 |')
print('|  105   |        X-Tudo         | 17,00 |')
print('|  200   |   Refrigerante Lata   |  5,00 |')
print('|  201   |       Chá Gelado      |  4,00 |')
while True:
  codigo=int(input('Entre com com o código desejado: ')) #Inserir o código do produto
  if codigo==100:
    print('Você pediu um Cachorro-Quente no valor de R$9,00')
    subtotal = subtotal + 9 #acumulador = acumulador + valor do produto
  elif codigo==101:
    print('Você pediu um Cachorro Quente Duplo no valor de R$11,00')
    subtotal = subtotal + 11 #acumulador = acumulador + valor do produto
  elif codigo==102:
    print('Você pediu um X-Egg no valor de R$12,00')
    subtotal = subtotal + 12 #acumulador = acumulador + valor do produto
  elif codigo==103:
    print('Você pediu um X-Salada no valor de R$13,00')
    subtotal = subtotal + 13 #acumulador = acumulador + valor do produto
  elif codigo==104:
    print('Você pediu um X-Bacon no valor de R$14,00')
    subtotal = subtotal + 14 #acumulador = acumulador + valor do produto
  elif codigo==105:
    print('Você pediu um X-Tudo no valor de R$17,00')
    subtotal = subtotal + 17 #acumulador = acumulador + valor do produto
  elif codigo==200:
    print('Você pediu um Refrigerante Lata no valor de R$5,00')
    subtotal = subtotal + 5 #acumulador = acumulador + valor do produto
  elif codigo==201:
    print('Você pediu um Chá Gelado no valor de R$4,00')
    subtotal = subtotal + 4 #acumulador = acumulador + valor do produto
  else:
    print('Opção Inválida') #se errar o código cai aqui
    continue #e cai no laço e volta para o início
  reposta = input('Deseja pedir mais alguma coisa? Digite "1" para Sim ou "0" para Não: ')
  if reposta == "1": #se desejar mais algum pedido
    continue
  else:
    print('O total a ser pago é: R${:.2f}'.format(subtotal)) #se não desejar mais nenhum pedido, encerrar a conta e dar o valor total
    break #fim do laço