import random
board = [' ',  ' ', ' ', ' ',' ',' ',' ',' ',' ']
gameRunning = False

def createBoard(board):
        print(
            f"""
                {board[0]} | {board[1]} | {board[2]}
                ----------
                {board[3]} | {board[4]} | {board[5]}
                ----------
                {board[6]} | {board[7]} | {board[8]}""")
    
def playerTic(board):
        correctPick = False
        while(not correctPick):
            inp = int(input('Choose a number between 1-9 [X]:'))
            if not (inp > 0 and inp <=9):
                print('Please choose your value between 1-9!')
            elif board[inp] != ' ':
                print('That Place is already taken, try again.')
            else:
                board[inp] = 'X'
                correctPick = True
                createBoard(board)

def computerTic(board):
    conditionMet = False
    while(not conditionMet):
        randomChoice = random.randint(0, 8)
        if board[randomChoice] == ' ':
            board[randomChoice] = 'O'
            conditionMet = True
            createBoard(board)
         
def checkWin(board):

     if board[0] == board[1] == board[2]:
          gameRunning = False
          print('The Winner is {}'.format(board[0]))
     elif board[3] == board[4] == board[5]:
        gameRunning = False
        print('The Winner is {}'.format(board[0]))
     elif board[6] == board[7] == board[8]:
        gameRunning = False
        print('The Winner is {}'.format(board[0]))
    
     if board[0] == board[4] == board[8]:
        gameRunning = False
        print('The Winner is {}'.format(board[0]))
     elif board[2] == board[4] == board[6]:
        gameRunning = False
        print('The Winner is {}'.format(board[0]))

     if board[0] == board[3] == board[6]:
        gameRunning = False
        print('The Winner is {}'.format(board[0]))
     elif board[1] == board[4] == board[7]:
        gameRunning = False
        print('The Winner is {}'.format(board[0]))
     elif board[2] == board[5] == board[8]:
        gameRunning = False
        print('The Winner is {}'.format(board[0]))
    
          
          
createBoard(board)
while(gameRunning):
    playerTic(board)
    checkWin(board)
    computerTic(board)
    checkWin(board)