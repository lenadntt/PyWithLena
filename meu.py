def criar_matriz(pos_player, invaders):
    matriz = [[' ' for _ in range(40)] for _ in range(40)]

    for i in range(38, 40):
        matriz[i] = ["###"] * 40

    for invader in invaders:
        matriz[invader[0]][invader[1]] = 'w'

    matriz[37][pos_player] = 'A'

    return matriz

def mostrar_matriz(matriz):
    for linha in matriz:
        print("".join(linha))

def mov_player(pos_player, direction):
    if direction == '4' and pos_player > 0:
        pos_player -= 1
    elif direction == '6' and pos_player < 39:
        pos_player += 1

    return pos_player

def checar_tiros(pos_player, invaders):
    for invader in invaders:
        if invader[1] == pos_player:  
            invaders.remove(invader)  
            print("Acertou um inimigo!")
            return True
    print("Atirou no ar!")
    return False

def adicionar_inimigos(invaders):
    direcao = 1
    nova_linha = [(0, i) for i in range(0, 40, 2)]  
    invaders = [(x + 1, y + direcao) for x, y in invaders]  
    invaders = nova_linha + invaders  
    
    invaders = [invader for invader in invaders if invader[0] < 38]

    return invaders

def verificar_derrota(invaders):
    for invader in invaders:
        if invader[0] >= 38:
            return True
    return False

def menu():
    global pos_player, invaders, game_over

    while not game_over:
        matriz = criar_matriz(pos_player, invaders)
        mostrar_matriz(matriz)

        if verificar_derrota(invaders):
            print("Os invasores alcançaram a base. Você perdeu!")
            game_over = True
            break

        opcao = input("0 - Encerrar \n1 - Mover \n2 - Disparar\nEscolha: ")

        if opcao == '0':
            game_over = True
            print("Pediu arrego!")
        elif opcao == '1':
            direction = input("4 - Esquerda, 6 - Direita: ")
            pos_player = mov_player(pos_player, direction)
        elif opcao == '2':
            if checar_tiros(pos_player, invaders):
                if not invaders:  
                    game_over = True
                    print("Você venceu!")
            else:
                print("Tente novamente!")

            
            invaders = adicionar_inimigos(invaders)
        else:
            print("Escolha inválida!")

if __name__ == "__main__":
    pos_player = 20
    invaders = [(0, i) for i in range(0, 40, 2)] 
    game_over = False

    menu()


