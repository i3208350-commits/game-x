def examination(x ):
    if  x in ["0","1","2","3" ,"4","5","6","7","8","9"]:
        return True
    return False

def Checking_empty(input_1,position,board):
    for i in board :
        if i[0]==position and i[1]== None:
             print("occupied")
             i[1] = input_1
             return board
    print("Space occupied, please choose again.")
    return

def draw(board):
    for i in board:
        if i[1] != None:
            print("The game ended in a draw!")
        break




def Victory_check(x,board):


   if (board[0][1]==x and board[1][1]==x and board[2][1]==x) or (board[3][1]==x and board[4][1]==x and board[5][1]==x) or (board[6][1]==x and board[7][1]==x and board[8][1]==x) or (board[0][1]==x and board[3][1]==x and board[6][1]==x) or (board[1][1]==x and board[4][1]==x and board[7][1]==x) or (board[0][1]==x and board[4][1]==x and board[8][1]==x) or (board[2][1]==x and board[4][1]==x and board [6][1]==x):
      return True
   return

def Board_printing(board):
    return board

def cek(count):
    if count % 2 == 0:
        input_1 = "x"
    else:
        input_1 = "o"
    return input_1







def Victory_print(input_1):

        return f"Congratulations!, you  {input_1}   won the game!!!"



def User_test(x):
    if x=="x" or x=="o":
        return True
    return False