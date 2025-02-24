'''1-) Dados o valor de uma conta em um restaurante (valor inteiro) e o valor do
pagamento, apresente o número mínimo de cédulas e moedas que deve ser
retornado como troco.'''

valor_conta = 150 #int(input("Digite. Quanto custou a sua conta? "))
pagamento = 250 #int(input("Digite. Com quanto você vai pagar? "))

notas = [200,100,50,20,10,5,2,1]
troco = pagamento - valor_conta
notas_usadas = []
for nota in notas:
    qtd_cedula = troco // nota
    troco = 

    print()