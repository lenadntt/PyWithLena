# Números primos: Escreva uma função que determine se um número é primo ou não.
num = int(input("Insira um número ao lado: "))

if num < 1:
    print("Por favor, insira um número inteiro positivo.")
else:
    primo = True  # Assume que o número é primo inicialmente

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False  # Se encontrar um divisor, não é primo
            break  # Sai do loop

    if primo:
        print(num, 'É primo!')
    else:
        print(num, 'Não é primo!')
# Validador de CPF: Crie um programa que valide se um CPF inserido é válido, utilizando as regras de cálculo de dígitos verificadores.
import re

cpf = input("Digite seu CPF: ")

def digitos_iguais(cpf):
    return cpf == cpf[0] * len(cpf)

def calcular_d_v(cpf, peso_inicial):
    soma = 0 
    for i in range(len(cpf)):
        soma += int(cpf[i]) * peso_inicial
        peso_inicial -= 1
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def verificar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  
    
    if len(cpf) != 11:
        print("CPF inválido: deve conter 11 dígitos.")
        return False
    
    if digitos_iguais(cpf):
        print("CPF inválido: todos os dígitos são iguais.")
        return False
    
    primeiro_dig = calcular_d_v(cpf[:9], 10)
    segundo_dig = calcular_d_v(cpf[:10], 11)

    if cpf[-2:] == f"{primeiro_dig}{segundo_dig}":
        return True
    else:
        return False

if verificar_cpf(cpf):
    print("CPF é válido!")
else:
    print("CPF inválido!")



    




# Matriz transposta: Escreva uma função que receba uma matriz (lista de listas) e retorne a sua transposta.
# Simulador de Caixas Eletrônicos: Crie um programa que simule a retirada de dinheiro de um caixa eletrônico, informando as cédulas disponíveis e minimizando o número de cédulas entregues.