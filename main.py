import play as p
board=[["1",None],["2",None],["3",None],
      ["4",None],["5",None],["6",None],
      ["7",None],["8",None],["9",None]]
def play():
    while True:
        input_1=input("Are you x or o?")
        p.User_test(input_1)
        position = input("Choose an index where you want to put your game tools.")
        p.examination(position)
        value = p.Checking_empty(input_1,position,board)
        print(value)
        if p.Victory_check(input_1,board):
            p.Victory_print()
            break
        print(p.Board_printing(board))




if __name__ == '__main__':
    play()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
