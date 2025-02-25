'''1-) Dados o valor de uma conta em um restaurante (valor inteiro) e o valor do
pagamento, apresente o número mínimo de cédulas e moedas que deve ser
retornado como troco.'''

valor_conta = int(input("Digite. Quanto custou a sua conta? "))
pagamento = int(input("Digite. Com quanto você vai pagar? "))

notas = [200,100,50,20,10,5,2,1]
troco = pagamento - valor_conta
notas_usadas = []
print(f'Seu troco é R${troco}')
for nota in notas:
    qtd_cedula = troco // nota
    troco =(troco - (qtd_cedula*nota))
    if qtd_cedula != 0:
        notas_usadas.append(nota)
    print(f'Quatidade notas de ${nota} : {qtd_cedula}')
print(f'Sugestão de troco:{notas_usadas}')