branco = " "
velha = [[' ' if numero % 2 == 0 else ' ' for numero in range(
    1, 4)] for valor in range(1, 4)]
token = ["X", "O"]


def criarBoard():
    return velha


def printBoard(board):
    for i in range(3):
        print('|'.join(board[i]))
        if(i < 2):
            print('------')
    print()


def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if n >= 1 and n <= 3:
            return n - 1
        else:
            print("Numero precisa estar entre 1 e 3")
            return getInputValido(mensagem)
    except:
        print('Número inválido')
        return getInputValido(mensagem)

def verificaMovimento(board, linha , coluna):
    if(board[linha][coluna] == branco):
        return True
    else:
        return False

def fazMovimento(board, linha, coluna, jogador):
    board[linha][coluna] = token[jogador]


def verificarGanhador(board):
    # Linha
    for linha in range(3):
        if board[linha][0] == board[linha][1] and board[linha][1] == board[linha][2] and board[linha][0] != branco:
            return board[linha][0]
    # Coluna
    for coluna in range(3):
        if board[0][coluna] == board[1][coluna] and board[1][coluna] == board[2][coluna] and board[0][coluna] != branco:
            return board[0][coluna]

    # Diagonal Principal
    if board[0][0] != branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    # Diagonal Secundária
    if board[0][2] != branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if board[i][j] == branco:
                return False
    return 'Empatou'