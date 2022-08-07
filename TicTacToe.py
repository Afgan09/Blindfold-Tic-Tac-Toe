import random
import os

clear = lambda: os.system('cls')
moveBot = ""
moveBotList = []
moveHumanList = []
listMoves = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
randomChance = ""
restart = True


def doesWin(moveList):
    isWinning = False
    if 'a1' in moveList and 'a2' in moveList and 'a3' in moveList:
        isWinning = True
    if 'b1' in moveList and 'b2' in moveList and 'b3' in moveList:
        isWinning = True
    if 'c1' in moveList and 'c2' in moveList and 'c3' in moveList:
        isWinning = True
    if 'a1' in moveList and 'b2' in moveList and 'c3' in moveList:
        isWinning = True
    if 'a3' in moveList and 'b2' in moveList and 'c1' in moveList:
        isWinning = True
    if 'a1' in moveList and 'b1' in moveList and 'c1' in moveList:
        isWinning = True
    if 'a2' in moveList and 'b2' in moveList and 'c2' in moveList:
        isWinning = True
    if 'a3' in moveList and 'b3' in moveList and 'c3' in moveList:
        isWinning = True
    return isWinning


def BotDefend(PlayerList, MovesAval, HumanMoves):

    if 'a1' in PlayerList and 'b2' in PlayerList and 'c3' in MovesAval:
        return "c3"
    if 'b2' in PlayerList and 'c3' in PlayerList and 'a1' in MovesAval:
        return "a1"
    if 'a1' in PlayerList and 'c3' in PlayerList and 'b2' in MovesAval:
        return "b2"

    if 'a3' in PlayerList and 'b2' in PlayerList and 'c1' in MovesAval:
        return "c1"
    if 'b2' in PlayerList and 'c1' in PlayerList and 'a3' in MovesAval:
        return "a3"
    if 'a3' in PlayerList and 'c1' in PlayerList and 'b2' in MovesAval:
        return "b2"

    if HumanMoves.find("a")!=-1:
        if 'a1' in PlayerList and 'a2' in PlayerList and 'a3' in MovesAval:
            return 'a3'
        if 'a1' in PlayerList and 'a3' in PlayerList and 'a2' in MovesAval:
            return "a2"
        if 'a2' in PlayerList and 'a3' in PlayerList and 'a1' in MovesAval:
            return "a1"

    if HumanMoves.find("b")!=-1:
        if 'b1' in PlayerList and 'b2' in PlayerList and 'b3' in MovesAval:
            return 'b3'
        if 'b1' in PlayerList and 'b3' in PlayerList and 'b2' in MovesAval:
            return "b2"
        if 'b2' in PlayerList and 'b3' in PlayerList and 'b1' in MovesAval:
            return "b1"

    if HumanMoves.find("c")!=-1:
        if 'c1' in PlayerList and 'c2' in PlayerList and 'c3' in MovesAval:
            return 'c3'
        if 'c1' in PlayerList and 'c3' in PlayerList and 'c2' in MovesAval:
            return "c2"
        if 'c2' in PlayerList and 'c3' in PlayerList and 'c1' in MovesAval:
            return "c1"

    if HumanMoves.find("1")!=-1:
        if 'a1' in PlayerList and 'b1' in PlayerList and 'c1' in MovesAval:
            return "c1"
        if 'a1' in PlayerList and 'c1' in PlayerList and 'b1' in MovesAval:
            return "b1"
        if 'c1' in PlayerList and 'b1' in PlayerList and 'a1' in MovesAval:
            return "a1"

    if HumanMoves.find("2")!=-1:
        if 'a2' in PlayerList and 'b2' in PlayerList and 'c2' in MovesAval:
            return "c2"
        if 'a1' in PlayerList and 'c2' in PlayerList and 'b2' in MovesAval:
            return "b2"
        if 'c1' in PlayerList and 'b2' in PlayerList and 'a2' in MovesAval:
            return "a2"

    if HumanMoves.find("3")!=-1:
        if 'a3' in PlayerList and 'b3' in PlayerList and 'c3' in MovesAval:
            return "c3"
        if 'a3' in PlayerList and 'c3' in PlayerList and 'b3' in MovesAval:
            return "b3"
        if 'c3' in PlayerList and 'b3' in PlayerList and 'a3' in MovesAval:
            return "a3"
    return ""

# Start of game

while True:
    if restart == True:
        clear()
        moveBotList = []
        moveHumanList = []
        listMoves = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        restart = False
        if random.randint(1, 3) == 2:
            moveBot = random.choice(listMoves)
            moveBotList.append(moveBot)
            i = listMoves.index(moveBot)
            listMoves[i] = "taken"
            print(moveBot)
    moveHuman = input("Move: ")
    if moveHuman not in listMoves:
        print("This move was already played! You lose!")
        input("Press ENTER to restart")
        continue

    moveHumanList.append(moveHuman)
    i = listMoves.index(moveHuman)
    listMoves[i] = "taken"
    if doesWin(moveHumanList) is True:
        print("You win!")
        input("Press ENTER to restart")
        restart = True
        continue
    if listMoves.count("taken") == 9:
        print("Draw!")
        input("Press ENTER to restart")
        restart = True
        continue

    #  Bot AI

    moveBot = BotDefend(moveHumanList, listMoves, moveHuman)
    if moveBot == "":
        while True:
            moveBot = random.choice(listMoves)
            if moveBot=="taken":
                continue
            break
        moveBotList.append(moveBot)
        i = listMoves.index(moveBot)
        listMoves[i] = "taken"
        print(moveBot)
        continue
    else:
        moveBotList.append(moveBot)
        i = listMoves.index(moveBot)
        listMoves[i] = "taken"
        print(moveBot)

    # is bot winning
    if doesWin(moveBotList) is True:
        print("Bot wins!")
        input("Press ENTER to restart")
        restart = True
        continue
    continue
