import re
from pprint import pprint
# Desafio 1 - Encontre a palavra simples
frase = 'Olá! sou uma frase simples'

resultado_desafio1 = re.search(r"simples", frase)
print(resultado_desafio1)

print()

# Desafio 2 - Encontre todas as ocorrências de 23 (os números juntos) e exatamente com esses valores
frases = ['dev123com',
'developer 123',
'dev = 123',
'dev = 1234',
'dev = 1337',
'dev = 9000']

resultado_desafio2 = [re.search(r"23", frase) for frase in frases]

for i,resultado in enumerate(resultado_desafio2):
    if resultado:
        print(f'A string "{frases[i]}" contém "23"')
    else:
        print(f'A string "{frases[i]}" NÃO contém "23"')

print()

# Desafio 3 - Encontre todos os valores onde o valor inicial é 2, porém o segundo valor você não conhece. ex: 23,24,26, etc.

resultado_desafio3 = [re.search(r"2\d", frase) for frase in frases]

for i,resultado in enumerate(resultado_desafio3):
    if resultado:
        print(f'A string "{frases[i]}" contém "2" seguido de um dígito.')
    else:
        print(f'A string "{frases[i]}" NÃO contém "2" seguido de um dígito')

print()

# Desafio 4 - Usando os valores a seguir, encontre os seguintes números por completo:
numeros = ['13.35.86','22.36.77','53.12.34']

resultado_desafio4 = [re.findall(r"\d\d\.\d\d\.\d\d", numero) for numero in numeros]
pprint(resultado_desafio4)

print()

# Desafio 5 - Encontre apenas as combinações de acordo com o descrito abaixo:
combinacoes = ['bah pular',
'tah encontrar',
'jah encontrar',
'nah encontrar',
'uai pular']

resultado_desafio5 = [re.findall(r"[tjn]ah", combinacao) for combinacao in combinacoes]
for resultado in resultado_desafio5:
    if resultado:
        print(resultado)

print()

# Desafio 6 - Encontre as combinações de acordo com o descrito abaixo:
telefones = ['(123)1234-1235',
'(123)1234-1235',
'(129)1234-1235',
'(129)1234-1235']

resultado_desafio6 = [re.findall(r"[(]123[)]\d{4}[-]\d{4}", telefone) for telefone in telefones]
for telefone in resultado_desafio6:
    if telefone:
        print(telefone)

print()

# Desafio 7 - Encontre apenas a sequência 1234 abaixo:
numero_1 = ['1234',
'6462']

resultado_desafio7 = [re.findall(r"[1-4]", numero) for numero in numero_1]
for numero in resultado_desafio7:
    if numero:
        print(numero)

print()

# Desafio 8 - Encontre apenas as letras iniciando de P a V:
letras = ['pqrstuv',
'wxyz',
'abcdefg']

resultado_desafio8 = [re.findall(r"[p-v]", letra) for letra in letras]
for letra in resultado_desafio8:
    if letra:
        print(letra)

print()

# Desafio 9 - Encontrar tanto pizzas enviadas como pizza enviadas
pedidos = ['2 pizzas enviadas',
'1 pizza enviada',
'3 pizzas enviadas']

resultado_desafio9 = [re.findall(r"pizzas? enviadas?", pizza) for pizza in pedidos]
for pizza in resultado_desafio9:
    if pizza:
        print(pizza)