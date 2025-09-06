# Hello World!: Escreva um programa que exiba "Hello, World!" na tela.
a = 'Hello World!'
print(a)

# Números pares e ímpares: Crie um programa que peça um número ao usuário e informe se ele é par ou ímpar.
num = int(input("Insira um número ao lado: "))
if num % 2 == 0:
    print("Esse número é par!")
else:
    print("Esse número é ímpar!")

# Conversor de temperatura: Escreva um programa que converta temperaturas de Celsius para Fahrenheit.
temp_cel = float(input("Escreva ao lado a temperatura em Celsius: "))
temp_fah = temp_cel * 1.8 + 32
print("Aqui está a temperatura em Fahrenheit ", temp_fah)

# Contagem de vogais: Peça uma palavra ao usuário e conte quantas vogais ela possui.
palavra = input("Arrocha uma plavritcha aí: ")
print(len(palavra))

# Calculadora simples: Implemente uma calculadora que faça operações de adição, subtração, multiplicação e divisão.
while True:
    num_1 = float(input("Arroche o primeiro número que você precisa para efetuar a operação: "))
    num_2 = float(input("Arroche o segundo número que você precisa para efetuar a operação: "))
    menu = input("Agora escolha sua operação:  \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão:  ")
    if menu == "1":
        print((num_1)+ (num_2))
    elif menu == "2":
        print((num_1) - (num_2))
    elif menu == "3":
        print((num_1) * (num_2))
    elif menu == "4":
        if num_2 != 0:
            print((num_1) / (num_2))
        else:
            print("Error: Divisão por 0 irmão!")
    else:
        print("Ta doidão? São só 5 números irmão, não é tão hard não!")

    continuar = input("Deseja realizar outra opração? (S / N) ").strip().lower()
    if continuar != "s":
        print("Finalizando o programa. Xau!!")
        break  
