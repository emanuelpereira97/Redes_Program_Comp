frase = input("Digite uma palavra ou frase: ")
frase_entrada = frase.lower().replace(" ","")
frase_invertida = frase_entrada[::-1]

if frase_entrada == frase_invertida:
    print(f'{frase} é palindromo.')
else:
    print(f'{frase} não é palindromo.')    