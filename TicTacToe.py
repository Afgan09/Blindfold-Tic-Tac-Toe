import random
import os
clear = lambda: os.system('cls')
moveBotList = []
moveHumanList = []
countMoves = 0
listMoves= ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
def doesWin(moveList):
    isWinning=False
    if 'a1' in moveList and 'a2' in moveList and 'a3' in moveList:
        isWinning=True
    if 'b1' in moveList and 'b2' in moveList and 'b3' in moveList:
        isWinning=True
    if 'c1' in moveList and 'c2' in moveList and 'c3' in moveList:
        isWinning=True
    if 'a1' in moveList and 'b2' in moveList and 'c3' in moveList:
        isWinning=True
    if 'a3' in moveList and 'b2' in moveList and 'c1' in moveList:
        isWinning=True
    if 'a1' in moveList and 'b1' in moveList and 'c1' in moveList:
        isWinning=True
    if 'a2' in moveList and 'b2' in moveList and 'c2' in moveList:
        isWinning=True
    if 'a3' in moveList and 'b3' in moveList and 'c3' in moveList:
        isWinning=True
    return isWinning

while True:
    moveHuman=input("Move: ")
    if moveHuman not in listMoves:
        print("That move was already played! You lose!")
        input("Press ENTER to restart")
        clear()
        moveBotList = []
        moveHumanList = []
        countMoves = 0
        listMoves = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        continue
    moveHumanList.append(moveHuman)
    listMoves.remove(moveHuman)
    countMoves+=1
    if doesWin(moveHumanList) is True:
        print("You win!")
        input("Press ENTER to restart")
        clear()
        moveBotList = []
        moveHumanList = []
        countMoves = 0
        listMoves = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        continue
    if countMoves==5:
        break
    moveBot=random.choice(listMoves)
    moveBotList.append(moveBot)
    listMoves.remove(moveBot)
    print(moveBot)
    if doesWin(moveBotList) is True:
        print("Bot wins!")
        input("Press ENTER to restart")
        clear()
        moveBotList = []
        moveHumanList = []
        countMoves = 0
        listMoves = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        continue
    continue


