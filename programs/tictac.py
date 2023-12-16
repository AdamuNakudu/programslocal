player1 = input('player 1 name: ')
player2 = input('player 2 name: ')

theBoard = {'top-L':' ', 'top-M':' ', 'top-R': ' ',
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
            'low-L':' ', 'low-M':' ', 'low-R':' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '|')
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '|')
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '|')
    
turn = player1
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Where to?')
    while True:
        move = input()
        if move not in theBoard:
            print('Please type correct coordinates')
        else:
            break
        
    theBoard[move] = turn
    if turn == player1:
        turn = player2
    else:
        turn = player1
 

printBoard(theBoard)
