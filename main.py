from jogo_da_velha import criarBoard, fazMovimento, getInputValido, printBoard, verificarGanhador, verificaMovimento

jogador = 0 # jogador 1
board = criarBoard()
ganhador = verificarGanhador(board)
while(not ganhador):
    printBoard(board)
    linha = getInputValido("Digite a linha: ")
    coluna = getInputValido("Digite a coluna: ")
    
    if(verificaMovimento(board, linha , coluna)):
        fazMovimento(board, linha, coluna, jogador)
        jogador = (jogador + 1) % 2 # Troca de jogador 0 para 1
    else:
        print()
        print("A posição informada, ja está ocupada")

        ganhador = verificarGanhador(board)

print('========================')
printBoard(board)
print(f'Ganhador =  {ganhador}')
print('========================')