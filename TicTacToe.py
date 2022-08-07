import random
moveBotList = []
moveHumanList = []
countMoves = 0
listMoves=["a1", "a2", "a3", "b1", "b2", "b3", "c1","c2","c3"]

def doesWin(moveList):
    isWinning=False
    if ('a1' and 'a2') in moveList:
        if 'a3' in moveList:
            isWinning=True
    elif ('b1' and 'b2') in moveList:
        if 'b3' in moveList:
            isWinning=True
    elif ('c1' and 'c2') in moveList:
        if 'c3' in moveList:
            isWinning=True
    elif ('a1' and 'b2') in moveList:
        if 'c3' in moveList:
            isWinning=True
    elif ('a3' and 'b2') in moveList:
        if 'c1' in moveList:
            isWinning=True
    elif ('a1' and 'b1') in moveList:
        if 'c1' in moveList:
            isWinning=True
    elif ('a2' and 'b2') in moveList:
        if 'c2' in moveList:
            isWinning=True
    elif ('a3' and 'b3') in moveList:
        if 'c3' in moveList:
            isWinning=True
    return isWinning

while True:
    moveHuman=input("Move: ")
    if moveHuman not in listMoves:
        print("That move was already played! You lose!")
        break
    moveHumanList.append(moveHuman)
    listMoves.remove(moveHuman)
    countMoves+=1
    if doesWin(moveHumanList) is True:
        print("You win!")
        break
    if countMoves==5:
        break

    while True:
        moveBot=random.choice(listMoves)
        if moveBot not in listMoves:
            continue
        else:
            moveBotList.append(moveBot)
            listMoves.remove(moveBot)
            break
    print(moveBot)
    if doesWin(moveBotList) is True:
        print("Bot wins!")
        break
    continue


