#1° questão
print('Bem Vindo(a) a Loja do Paulo Vinicius Sales Moura')
produto = float(input('Insira o valor do produto:'))
qntd = int(input('Insira o valor da quantidade:'))
valorsemdesconto = produto * qntd #valorbruto
desconto5 = valorsemdesconto*0.05 #valortotal*5%, desconto de 5%
desconto5por100 = valorsemdesconto-desconto5 #desconto5%
desconto10 = valorsemdesconto*0.1 #valortotal*l0%, desconto de 10%
desconto10por100 = valorsemdesconto-desconto10 #desconto10%
desconto15 = valorsemdesconto*0.15 #valortotal*15%, desconto de 15%
desconto15por100 = valorsemdesconto-desconto15 #desconto15%
if qntd <= 9: #valor de 1 até 9 cai aqui (não tem desconto)
    print('O valor foi: R${:.2f}'.format(valorsemdesconto)) #print valor
elif 10 <= qntd <= 99: #valor de 10 até 99 cai aqui
    print('O valor sem o desconto foi: R${:.2f}'.format(valorsemdesconto)) #print valor sem desconto
    print('O valor com desconto foi: R${:.2f}'.format(desconto5por100),'(Desconto 5%)') #print valor com desconto 5%
elif 100 <= qntd <= 999: #valor de 100 até 999 cai aqui
    print('O valor sem o desconto foi: R${:.2f}'.format(valorsemdesconto)) #print valor sem desconto
    print('O valor com desconto foi: R${:.2f}'.format(desconto10por100),'(Desconto 10%)') #print valor com desconto 10%

elif qntd >= 1000: #qualquer valor acima de 1000 cai aqui
    print('O valor sem o desconto foi: R${:.2f}'.format(valorsemdesconto)) #print valor sem desconto
    print('O valor com desconto foi: R${:.2f}'.format(desconto15por100),'(Desconto 15%)') #print valor com desconto 15%