# Fatorial de um número: Escreva um programa que calcule o fatorial de um número dado pelo usuário.
num = int(input("Escreva um número para calcularmos sua fatorial: "))
result = 1
contador = 1

while contador <= num:
    result *= contador
    contador += 1
print("O resultado de {}! é: {}".format(num, result))
# Sequência de Fibonacci: Gere a sequência de Fibonacci até o enésimo número fornecido pelo usuário.       
n = int(input("Quantos termos da sequência de Fibonacci você quer? "))
fibonacci = [0, 1]
for i in range(2, n):
    prox_termo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(prox_termo)
print(f"Os primeiros {n} termos da sequência de Fibonacci são: {fibonacci}")
# Palíndromo: Crie um programa que verifique se uma palavra é um palíndromo (se lê da mesma forma de trás para frente).
def palindromo(texto):
    texto = ''.join(c for c in texto if c.isalnum()).lower()
    return texto == texto[::-1]

palavra = input("Digite uma palavra ou frase: ")
if palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
# Ordenação de lista: Peça ao usuário uma lista de números e ordene-a em ordem crescente sem usar funções prontas como sorted()
n = int(input("Quantos números você quer inserir? "))
lista = []

for i in range(n):
    nume = int(input("Digite um número: "))
    lista.append(nume)

for i in range(1, len(lista)):
    chave = lista[i]
    j = i - 1

    while j >= 0 and chave < lista[j]:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = chave

print("Lista ordenada: ", lista)        
# Contagem de palavras: Escreva um programa que leia um texto e conte quantas palavras ele contém.
text = str(input("Digite um texto que contaremos as palavras: "))
palavras = text.split()
total_palavras = len(palavras)
print(f"Total de palavras: {total_palavras}")