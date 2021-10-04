"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    qtdx = 0
    qtdo = 0

    # contando qtos X e qtos O tem no tabuleiro para saber quem irá jogar
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                qtdx += 1
            if board[i][j] == O:
                qtdo += 1

    # se a qtd de X for maior que Y, O joga. Senão é X inclusive X é o que inicia o jogo.
    if qtdx > qtdo:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilidades = set()

    # varrendo o array na busca de posições vazias
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibilidades.add((i, j))

    return possibilidades


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultado = copy.deepcopy(board)

    try:
        if resultado[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            # atualizando o valor
            resultado[action[0]][action[1]] = player(board)
            return resultado
    # tratando o erro
    except IndexError:
        print('Posição já preenchida')

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Buscando ganhador na linha
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != EMPTY:
                return board[i][0]

        # Buscando ganhador na coluna
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != EMPTY:
                return board[0][i]

    # Buscando ganhador nas diagonais
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != EMPTY:
            return board[0][0]

    if board[2][0] == board[1][1] == board[0][2]:
        if board[0][2] != EMPTY:
            return board[0][2]

    # Não encontrou ganhador
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # verificando se há um ganhador
    if winner(board) != None:
        return True
    else:
        # varrendo o array na busca de posições vazias, se tiver jogo não terminou
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False

    # não tendo mais posições vazias nem ganhador jogo terminou
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Verificando se jogo terminou
    if terminal(board):
        # efetuando os retornos do ganhador
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            v_minimo = float('-inf')
            for possibilidades in actions(board):
                i = valorMinimo(result(board, possibilidades))
                if i > v_minimo:
                    v_minimo = i
                    movimento = possibilidades
        else:
            v_maximo = float('inf')
            for possibilidades in actions(board):
                i = valorMaximo(result(board, possibilidades))
                if i < v_maximo:
                    v_maximo = i
                    movimento = possibilidades

    return movimento


def valorMinimo(board):
    if terminal(board):
        return utility(board)

    v_minimo = float('inf')

    # passando por todas as possibilidades e recuperando o menor valor
    for possibilidades in actions(board):
        v_minimo = min(v_minimo, valorMaximo(result(board, possibilidades)))

    return v_minimo


def valorMaximo(board):
    if terminal(board):
        return utility(board)

    v_maximo = float('-inf')

    # passando por todas as possibilidades e recuperando o maior valor
    for possibilidades in actions(board):
        v_maximo = max(v_maximo, valorMinimo(result(board, possibilidades)))

    return v_maximo
