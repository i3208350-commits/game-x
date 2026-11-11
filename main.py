import play as p
board=[["1",None],["2",None],["3",None],
      ["4",None],["5",None],["6",None],
      ["7",None],["8",None],["9",None]]

def play():
    count=0

    while True:
                print(p.Board_printing(board))
                input_1=p.cek(count)
                print(f"The player's turn:{input_1}")
                position = input("Choose an index where you want to put your game tools.")
                if not p.examination(position):
                    continue
                if not p.Checking_empty(input_1,position,board):
                    continue
                if p.Victory_check(input_1,board):
                    print(p.Victory_print(input_1))
                    break
                if p.draw(board):
                    break
                count += 1
if __name__ == '__main__':
    play()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
