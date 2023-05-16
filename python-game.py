import random
board = [' ',  ' ', ' ', ' ',' ',' ',' ',' ',' ']
gameRunning = True
gameWin = False
def createBoard(board):
        print(
            f"""
                {board[0]} | {board[1]} | {board[2]}
                ----------
                {board[3]} | {board[4]} | {board[5]}
                ----------
                {board[6]} | {board[7]} | {board[8]}""")
    
def playerTic(board):
        while(True):
            inp = int(input('Choose a number between 1-9 [X]:'))
            if not (inp > 0 and inp <=9):
                print('Please choose your value between 1-9!')
            elif board[inp-1] != ' ':
                print('That Place is already taken, try again.')
            else:
                board[inp-1] = 'X'
                createBoard(board)
                checkWin()
                break
                

def computerTic(board):
    while(True):
        randomChoice = random.randint(0, 8)
        if board[randomChoice] == ' ':
            board[randomChoice] = 'O'
            conditionMet = True
            createBoard(board)
            checkWin()
            break
            
         
def checkWin():
     global gameRunning
     global gameWin
     if board[0] == board[1] == board[2] and board[0] != ' ':
          gameRunning = False
          print('The Winner is {}'.format(board[0]))
     elif board[3] == board[4] == board[5] and board[3] != ' ':
        gameRunning = False
        print('The Winner is {}'.format(board[3]))
     elif board[6] == board[7] == board[8] and board[6] != ' ':
        gameRunning = False
        print('The Winner is {}'.format(board[6]))
    
     if board[0] == board[4] == board[8] and board[0] != ' ':
        gameRunning = False
        print('The Winner is {}'.format(board[0]))
     elif board[2] == board[4] == board[6] and board[2] != ' ':
        gameRunning = False
        print('The Winner is {}'.format(board[2]))

     if board[0] == board[3] == board[6] and board[0] != ' ':
        gameRunning = False
        print('The Winner is {}'.format(board[1]))
     elif board[1] == board[4] == board[7] and board[1] != ' ':
        gameRunning = False
        print('The Winner is {}'.format(board[1]))
     elif board[2] == board[5] == board[8] and board[2] != ' ':
        gameRunning = False
        print('The Winner is {}'.format(board[2]))
     if gameRunning == False:
         gameWin = True
     else: 
         checkTie()


def checkTie():
    global gameRunning, gameWin
    if ' ' not in board and gameWin == False:
        print("It's a tie!")
        gameRunning = False
        
createBoard(board)
while(gameRunning):
    computerTic(board)
    playerTic(board)
    