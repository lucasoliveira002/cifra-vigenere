#função para pegar as letras e transpor para numeros
def numeros (letra):
    if letra == "a":
        letra = 0
    elif letra == "b":
        letra = 1
    elif letra == "c":
        letra = 2
    elif letra == "d":
        letra = 3
    elif letra == "e":
        letra = 4
    elif letra == "f":
        letra = 5
    elif letra == "g":
        letra = 6
    elif letra == "h":
        letra = 7
    elif letra == "i":
        letra = 8
    elif letra == "j":
        letra = 9
    elif letra == "k":
        letra = 10
    elif letra == "l":
        letra = 11
    elif letra == "m":
        letra = 12
    elif letra == "n":
        letra = 13
    elif letra == "o":
        letra = 14
    elif letra == "p":
        letra = 15
    elif letra == "q":
        letra = 16
    elif letra == "r":
        letra = 17
    elif letra == "s":
        letra = 18
    elif letra == "t":
        letra = 19
    elif letra == "u":
        letra = 20
    elif letra == "v":
        letra = 21
    elif letra == "w":
        letra = 22
    elif letra == "x":
        letra = 23
    elif letra == "y":
        letra = 24
    elif letra == "z":
        letra = 25
    return letra
#função para pegar os números e transpor para letras
def reverter(total):
    if total == 0:
        total = "a"
    elif total == 1:
        total = "b"
    elif total == 2:
        total = "c"
    elif total == 3:
        total = "d"
    elif total == 4:
        total = "e"
    elif total == 5:
        total = "f"
    elif total == 6:
        total = "g"
    elif total == 7:
        total = "h"
    elif total == 8:
        total = "i"
    elif total == 9:
        total = "j"
    elif total == 10:
        total = "k"
    elif total == 11:
        total = "l"
    elif total == 12:
        total = "m"
    elif total == 13:
        total = "n"
    elif total == 14:
        total = "o"
    elif total == 15:
        total = "p"
    elif total == 16:
        total = "q"
    elif total == 17:
        total = "r"
    elif total == 18:
        total = "s"
    elif total == 19:
        total = "t"
    elif total == 20:
        total = "u"
    elif total == 21:
        total = "v"
    elif total == 22:
        total = "w"
    elif total == 23:
        total = "x"
    elif total == 24:
        total = "y"
    elif total == 25:
        total = "z"
    return total

mensagem = input("Escreva a palavra a ser criptografada:")
chave = input("Qual será a chave?")

tamanho = len(mensagem)
valores = []

#teste
tamanho_chave = len(chave)

#laço para separar e tranformar em numeros a mensagem
for letras in mensagem:
    valores.append(numeros(letras))

chave_numerica = [] 
for letras in chave:
    chave_numerica.append(numeros(letras))

#criando mensagem criptografada
n = 0
i = 0
total = []
while n < tamanho:    
    if i > tamanho_chave - 1:
        i = 0
        total.append(chave_numerica[i] + valores[n])
        i = i + 1
    else:
        total.append(chave_numerica[i] + valores[n])
        i = i + 1
    n = n + 1

#traduzindo mensagem criptografada
p = 0
codificada = []
for p in range(tamanho):
    if total[p] > 25:
        total[p] = total[p] - 26
    codificada.append(reverter(total[p]))

print(*codificada)