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
    moves = 0

    if terminal(board):
        return EMPTY

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != EMPTY:
                moves += 1

    if moves % 2 == 0:
        return X
    else:
        return O

    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return EMPTY
    
    actions = set()

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions.add((i,j))
            else:
                continue

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)

    if board[action[0]][action[1]] in {O, X}:
        raise NameError("Invalid Action!")
    elif board[action[0]][action[1]] == EMPTY:
        pass

    if player(board) == X:
        board_copy[action[0]][action[1]] == X
    elif player(board) == O:
        board_copy[action[0]][action[1]] == O

    return board_copy




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal
    for i in range(len(board)):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
    
    # Vertical
    for i in range(len(board)):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O

    # Diagonal
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """  
    moves = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != EMPTY:
                moves += 1

    if winner(board) != None:
        return True
    elif moves == 9:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif winner(board) == None:
        return 0


def minimax(board):
    Actions = actions(board)
    Player = player(board)
    action_score = {}

    if X in Player:
        action_score = {}
        for Action in Actions:
           action_score[Action] = calculate_score_for_board(board, Action) 
        max_score = -10
        for Action in Actions:
            if max_score < action_score[Action]:
                max_score = action_score[Action]
        return action_score[max_score] 
    elif O in Player:
        action_score = {}
        for Action in Actions:
           action_score[Action] = calculate_score_for_board(board, Action) 
        min_score = 10
        for Action in Actions:
            if min_score > action_score[Action]:
                min_score = action_score[Action]
        return action_score[min_score] 


def calculate_score_for_board(board, action):
    new_board_state =  result(board, action)
    if terminal(new_board_state):
        return utility(new_board_state)
    else:
        Actions = actions(new_board_state)
        for Action in Actions:
            score = calculate_score_for_board(new_board_state, Action)
            return score