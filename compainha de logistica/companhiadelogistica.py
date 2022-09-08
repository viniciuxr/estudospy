              #IDENTIFICADOR SE ENCONTRA NO INICIO DA MAIN
#------------------COMEÇO DA FUNÇÃO DIMENSOES OBJETO-----------------------
def dimensoes_objeto():
  while True:
    try:
      comprimento= float(input('Digite o comprimento do objeto (em cm): '))
      largura = float(input('Digite a largura do objeto (em cm): '))
      altura = float(input('Digite a altura do objeto (em cm): '))

      volume = altura * largura * comprimento

      if volume < 1000:
        return 10, volume
        print("o volume foi de {}".format(volume))
      elif 1000 <= volume < 10000:
        return 20, volume
        print("o volume foi de {}".format(volume))
      elif 10000 <= volume < 30000:
        return 30, volume
        print("o volume foi de {}.".format(volume))
      elif 30000 <= volume < 100000:
        return 50, volume
        print(f"o volume foi de {volume}")
      elif volume >= 100000:
        print(f"o volume do objeto é (em cm³) {volume}")
        print('Não aceitamos objetos com dimensões tão grandes.\nEntre com as dimensões desejadas novamente.\n>>5')
        continue
    except ValueError:
      print('Você digitou alguma dimensão do objeto com um valor não numérico\nPor favor entre com as dimensões desejada novamente.\n>>')
      continue
#------------------FINAL DA FUNÇÃO DIMENSOES OBJETO-----------------------
#------------------COMEÇO DA FUNÇÃO PESO OBJETO---------------------------
def peso_objeto():
  while True:
    try:
      peso= float(input('Digite o peso do objeto (em kg): '))


      if peso <= 0.1:
        return 1.0
      elif 0.1 < peso <= 1:
        return 1.5
      elif 1 < peso <= 10:
        return 2.0
      elif 10 < peso <= 30:
        return 3.0
      elif peso > 30:
        print('Não aceitamos objetos tão pesados.\nEntre com o peso desejado novamente.\n>>')
        continue
    except ValueError:
      print('Você digitou o peso com um valor não numérico\nPor favor entre com o peso desejado novamente.\n>>')
      continue
#---------------------------FINAL DA FUNÇÃO PESO OBJETO------------------------
#---------------------------COMEÇO DA FUNÇÃO ROTA OBJETO-----------------------
def rota_objeto():
  while True:
    print('Selecione a rota:\nRS - De Rio de Janeiro para São Paulo\nSB - De São Paulo para Brasília\nRB - De Rio de Janeiro para Brasília\n>>')
    try:
      rota=input('Selecione a rota: ')


      if rota == 'RS':
        return 1.0
      elif rota == 'SB':
        return 1.2
      elif rota == 'RB':
        return 1.5
        continue
      else:
        print('Você digitou uma rota que não existe\nPor favor entre com a rota desejada novamente.\n>>')
    except ValueError:
      print('Você digitou uma rota que não existe\nPor favor entre com a rota desejada novamente.\n>>')
      continue
#---------------------------FINAL DA FUNÇÃO ROTA OBJETO-------------------------------------------------
#----------------------------------COMEÇO DA MAIN-------------------------------------------------------------
print('Bem vindo a Companhia de Logística Paulo Vinicius Sales Moura')
dimensao, teste = dimensoes_objeto()
peso = peso_objeto()
rota = rota_objeto()
total = dimensao * peso * rota

print("Total a pagar(R$): {:.2f} (dimensões: {} * peso: {} * rota: {})".format(total, dimensao, peso, rota))
#----------------------------FIM DA MAIN------------------------------
