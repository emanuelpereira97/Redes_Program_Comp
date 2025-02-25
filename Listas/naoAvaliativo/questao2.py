'''2) Receba como entrada os coeficientes (inteiros) de uma equação de segundo grau:
a, b e c, e apresente as raízes reais.'''

a= 1 #int(input("Digite um valor inteiro para o coeficiente a: "))
b= 4 #int(input("Digite um valor inteiro para o coeficiente b: "))
c= 1 #int(input("Digite um valor inteiro para o coeficiente c: "))

delta = (b*b) - (4*a*c) 
if (delta > 0 or delta == 0):

    print(delta)