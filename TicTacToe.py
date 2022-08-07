import random
import os
clear = lambda: os.system('cls')
moveBot=""
moveBotList = []
moveHumanList = []
listMoves= ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
randomChance=""
restart=False
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

#Start of game
while True:
    if restart==True:
        clear()
        moveBotList = []
        moveHumanList = []
        listMoves = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        restart=False
    if random.randint(1,2)==2 and len(listMoves)==9:
        moveBot = random.choice(listMoves)
        moveBotList.append(moveBot)
        i = listMoves.index(moveBot)
        listMoves[i] = "taken"
        print(moveBot)
    moveHuman=input("Move: ")
    if moveHuman not in listMoves:
        print("This move was already played! You lose!")
        input("Press ENTER to restart")
        continue

    moveHumanList.append(moveHuman)
    i=listMoves.index(moveHuman)
    listMoves[i] = "taken"
    if doesWin(moveHumanList) is True:
        print("You win!")
        restart=True
        continue
    if listMoves.count("taken")==9:
        print("Draw!")
        input("Press ENTER to restart")
        restart=True
        continue

       #  Bot AI

    if moveHuman.find("a")!=-1:
        while True:
            randomChance=random.choice(listMoves[0:5])
            if randomChance=="taken":
                continue
            else:
                moveBot=randomChance
                break
    elif moveHuman.find("b")!=-1:
        while True:
            randomChance=random.choice(listMoves[0:9])
            if randomChance=="taken":
                continue
            else:
                moveBot=randomChance
                break
    elif moveHuman.find("c")!=-1:
        while True:
            randomChance=random.choice(listMoves[4:9])
            if randomChance=="taken":
                continue
            else:
                moveBot=randomChance
                break
    moveBotList.append(moveBot)
    listMoves.remove(moveBot)
    print(moveBot)

# is bot winning
    if doesWin(moveBotList) is True:
        print("Bot wins!")
        input("Press ENTER to restart")
        restart = True
        continue
    continue
