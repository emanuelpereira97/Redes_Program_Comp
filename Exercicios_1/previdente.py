capitalInicial = float(input("Digite seu capinal inicial: "))
aporteMensal = float(input("Digite o valor do aporte mensal: "))
taxaMensal = float(input("Digite o valor da taxa de juros mensal: "))
numeroMeses = int(input("Digite a quantidade de meses: "))

t0 = taxaMensal/100

t1 = 1 + t0

t2 = t1**numeroMeses

valorInvestido = capitalInicial + (aporteMensal*numeroMeses)

saldo = capitalInicial * t2 + aporteMensal*((t2 - t1)/t0)

ganhoJuros = saldo - valorInvestido

print ("O saldo é de: R$",round(saldo,2), ". O valor investido é de: R$",round(valorInvestido,2), ". Você ganhou: R$",round(ganhoJuros,2), " com juros")