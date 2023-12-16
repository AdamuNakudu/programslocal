def print_board(board):
    for row in board:
        print(" | ".join(row))
        print(" -" * 4)
        
def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    return None
        
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def play_tic():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    
    while True:
        print_board(board)
        row = int(input(f"Player {player} enter row"))
        col = int(input(f"Player {player} enter column"))
        
        if board[row][col] == ' ':
            board[row][col] = player
            winner = check_winner(board)
            
            if winner:
                print_board(board)
                print(f"Player {winner} wins")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a Tie!")
                break
            
            player = '0' if player == 'X' else 'X'
            
        else:
            print("Cell occupied")

if __name__ == "__main__":
    play_tic()