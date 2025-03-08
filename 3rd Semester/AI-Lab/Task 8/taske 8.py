# taske 8 Minimax Algorithm Implementation
import math
PLAYER_X='X'
PLAYER_O='O'
EMPTY=' '

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board):
    for row in board:
        if row[0]==row[1]==row[2] !=EMPTY:
            return row[0]
    
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] !=EMPTY:
            return board[0][col]
    
    if board[0][0]==board[1][1]==board[2][2] !=EMPTY:
        return board[0][0]
    
    if board[0][2]==board[1][1]==board[2][0] !=EMPTY:
        return board[0][2]
    
    return None

def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner=check_winner(board)
    if winner==PLAYER_X:
        return 1
    elif winner==PLAYER_O:
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score=-math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col]==EMPTY:
                    board[row][col]=PLAYER_X
                    score=minimax(board, depth + 1, False)
                    board[row][col]=EMPTY
                    best_score=max(score, best_score)
        return best_score
    else:
        best_score=math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col]==EMPTY:
                    board[row][col]=PLAYER_O
                    score=minimax(board, depth + 1, True)
                    board[row][col]=EMPTY
                    best_score=min(score, best_score)
        return best_score

def find_best_move(board):
    best_score=-math.inf
    best_move=(-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col]==EMPTY:
                board[row][col]=PLAYER_X
                score=minimax(board, 0, False)
                board[row][col]=EMPTY
                if score > best_score:
                    best_score=score
                    best_move=(row, col)

    return best_move

if __name__=="__main__":
    board=[
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

    print("Initial Board:")
    print_board(board)

    while True:
        move=find_best_move(board)
        if move !=(-1, -1):
            board[move[0]][move[1]]=PLAYER_X
            print("\nAI (X) makes a move:")
            print_board(board)

            if check_winner(board):
                print("AI (X) wins!")
                break
            if is_board_full(board):
                print("It's a draw!")
                break

        row, col=map(int, input("Enter your move (row and column): ").split())
        if board[row][col]==EMPTY:
            board[row][col]=PLAYER_O
            print("\nPlayer O makes a move:")
            print_board(board)

            if check_winner(board):
                print("Player O wins!")
                break
            if is_board_full(board):
                print("It's a draw!")
                break
        else:
            print("Invalid")