import time
import os
import tictactoe
import minesweeper
import menu

def cls():
    cls = os.system('cls')

ans = True
while ans:
    cls()
    menu.showmenu()
    selection = int(input("Choice your option: "))
    if selection == 1:
        cls()
        ttt = tictactoe.tictactoegame()
        ttt.game()
    elif selection == 2:
        cls()
        ms = minesweeper.minesweepergame()
        ms.game()
        continue
    elif selection == 0:
        ans = False
        break
    else:
        print("Unknown option selected!")
        time.sleep(3)



