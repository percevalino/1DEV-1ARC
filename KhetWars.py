#Variables :
#board : plateau
#player : joueur qui joue
#i : ligne où va le pion
#j : colonne ou va le pion
#y : ligne où est le pion
#x : colonne où est le pion
#sensRotation : sens de la rotation du pion à effectuer, 0:anti horaire, 1:horaire


#Numéros pions :
#1 : Pharaoh
#2 : Scarab
#3 : Anubis
#4 : Pyramid
#5 : Sphinx


#disposition case :
#[1 ou 2 selon joueur, numéro du type de pion, orientation du pion]


def possible(board,player,x,y,i,j):#à refaire (if dans des for, parcours 9 cases autour sans milieu
    if board[i-1][j-1][0] == 0:
        return True
    elif board[i-1][j-1][0] == player:
        if board[y-1][x-1][1] == 2:
            if board[i-1][j-1][1] == 3 or board[i-1][j-1][1] == 4:
                return True
    return False


def put(board,player,x,y,i,j):
    if board[y-1][x-1][1] == 2:
        board[i-1][j-1],board[y-1][x-1] = board[y-1][x-1],board[i-1][j-1]
    else:
        board[i-1][j-1] = board[y-1][x-1]
        board[y-1][x-1] = [0, 0, "n"]


def win(board,player):
    for i in range(8):
        for j in range(10):
            if board[i][j][1] == 1:
                if board[i][j][0] != player:
                    return False
    return True


def rotation(board,x,y,sensRotation):
    if board[y-1][x-1][2] == "n":
        if sensRotation == 0:
            board[y-1][x-1][2] = "o"
        else:
            board[y-1][x-1][2] = "e"
        
    if board[y-1][x-1][2] == "s":
        if sensRotation == 0:
            board[y-1][x-1][2] = "e"
        else:
            board[y-1][x-1][2] = "o"
        
    if board[y-1][x-1][2] == "e":
        if sensRotation == 0:
            board[y-1][x-1][2] = "n"
        else:
            board[y-1][x-1][2] = "s"
        
    if board[y-1][x-1][2] == "o":
        if sensRotation == 0:
            board[y-1][x-1][2] = "s"
        else:
            board[y-1][x-1][2] = "n"



def laser(board,player):
    if player == 1:
        lx = 9
        ly = 7
        dx = 0
        dy = -1
    else:
        lx = 0
        ly = 0
        dx = 0
        dy = 1
        
    laserList = []
    laserOn = True
    
    while laserOn:
        hit = False
        lx += dx
        ly += dy
        if board[ly][lx][0] != 0:
            
            if board[ly][lx][1] == 5 and board[ly][lx][0] != player:#sphinx
                laserOn = False
                
            elif board[ly][lx][1] == 1 and board[ly][lx][0] != player:#pharaoh -> player loss
                board[ly][lx] = [0,0,"n"]
                laserOn = False
                
            elif board[ly][lx][1] == 4:#pyramid
                if dy == -1:
                    if board[ly][lx][0] != player:
                        if board[ly][lx][2] == "n" or board[ly][lx][2] == "o":
                            board[ly][lx] = [0,0,"n"]
                            laserOn == False
                    elif board[ly][lx][2] == "e":
                        dy = 0
                        dx = 1
                    elif board[ly][lx][2] == "s":
                        dy =0
                        dx = -1

                elif dy == 1:
                    if board[ly][lx][0] != player:
                        if board[ly][lx][2] == "e" or board[ly][lx][2] == "s":
                            board[ly][lx] == [0,0,"n"]
                            laserOn = False
                    elif board[ly][lx][2] == "n":
                        dy = 0
                        dx = 1
                    elif board[ly][lx][2] == "o":
                        dy = 0
                        dx = -1

                elif dx == 1:
                    if board[ly][lx][0] != player:
                        if board[ly][lx][2] == "e" or board[ly][lx][2] == "n":
                            board[ly][lx] == [0,0,"n"]
                            laserOn = False
                    elif board[ly][lx][2] == "s":
                        dx = 0
                        dy = 1
                    elif board[ly][lx][2] == "o":
                        dx = 0
                        dy = -1

                elif dx == -1:
                    if board[ly][lx][0] != player:
                        if board[ly][lx][2] == "s" or board[ly][lx][2] == "o":
                            board[ly][lx] == [0,0,"n"]
                            laserOn = False
                    elif board[ly][lx][2] == "e":
                        dx = 0
                        dy = 1
                    elif board[ly][lx][2] == "n":
                        dx = 0
                        dy = -1
                
                     
            elif board[ly][lx][1] == 3:#anubis
                if dy == 1:
                    if board[ly][lx][0] != player:
                        if board[ly][lx][2] == "s":
                            board[ly][lx] == [0,0,"n"]
                            laserOn = False
                    else:
                        laserOn = False

                elif dy == -1:
                    if board[ly][lx][0] != player:
                        if board[ly][lx][2] == "n":
                            board[ly][lx] == [0,0,"n"]
                            laserOn = False
                    else:
                        laserOn = False

                elif dx == 1:
                    if board[ly][lx][0] != player:
                        if board[ly][lx][2] == "e":
                            board[ly][lx] = [0,0,"n"]
                            laserOn = False
                    else:
                        laserOn = False

                elif dx == -1:
                    if board[ly][lx][0] != player:
                        if board[ly][lx][2] == "o":
                            board[ly][lx] = [0,0,"n"]
                            laserOn = False
                    else:
                        laserOn = False

            elif board[ly][lx][1] == 3:#scarab
                if dy == 1:
                    if board[ly][lx][2] == "n" or board[ly][lx][2] == "s":
                        dy = 0
                        dx = 1
                    elif board[ly][lx][2] == "e" or board[ly][lx][2] == "o":
                        dy = 0
                        dx = -1

                if dy == -1:
                    if board[ly][lx][2] == "n" or board[ly][lx][2] == "s":
                        dy = 0
                        dx = -1
                    elif board[ly][lx][2] == "e" or board[ly][lx][2] == "o":
                        dy = 0
                        dx = 1

                if dx == 1:
                    if board[ly][lx][2] == "n" or board[ly][lx][2] == "s":
                        dy = 1
                        dx = 0
                    elif board[ly][lx][2] == "e" or board[ly][lx][2] == "o":
                        dy = -1
                        dx = 0

                if dx == -1:
                    if board[ly][lx][2] == "n" or board[ly][lx][2] == "s":
                        dy = -1
                        dx = 0
                    elif board[ly][lx][2] == "e" or board[ly][lx][2] == "o":
                        dy = 1
                        dx = 0

        laserList.append([lx,ly])

        if lx == 9 and dx == 1 or lx == 0 and dx == -1 or ly == 9 and dy == 1 or ly == 0 and dy == -1:
            laserOn = False


def loadBoard(mapChoice):
    if mapChoice == 1:#classic
        board = [[[2, 5, 's'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [2, 3, 's'], [2, 1, 's'], [2, 3, 's'], [2, 4, 'e'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [2, 4, 's'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 4, 'o'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[2, 4, 'n'], [0, 0, 'n'], [1, 4, 's'], [0, 0, 'n'], [2, 2, 'n'], [2, 2, 'e'], [0, 0, 'n'], [2, 4, 'e'], [0, 0, 'n'], [1, 4, 'o']], [[2, 4, 'e'], [0, 0, 'n'], [1, 4, 'o'], [0, 0, 'n'], [1, 2, 'o'], [1, 2, 's'], [0, 0, 'n'], [2, 4, 'n'], [0, 0, 'n'], [1, 4, 's']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [2, 4, 'e'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 4, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [1, 4, 'o'], [1, 3, 'n'], [1, 1, 'n'], [1, 3, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 5, 'n']]]
    elif mapChoice == 2:#imhotep
        board = [[[2, 5, 's'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [2, 3, 's'], [2, 1, 's'], [2, 3, 's'], [2, 2, 'e'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 4, 'o'], [0, 0, 'n'], [0, 0, 'n'], [2, 4, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[2, 4, 'n'], [1, 4, 's'], [0, 0, 'n'], [0, 0, 'n'], [1, 4, 'e'], [2, 2, 'e'], [0, 0, 'n'], [0, 0, 'n'], [2, 4, 'e'], [1, 4, 'o']], [[2, 4, 'e'], [1, 4, 'o'], [0, 0, 'n'], [0, 0, 'n'], [1, 2, 'o'], [2, 4, 'o'], [0, 0, 'n'], [0, 0, 'n'], [2, 4, 'n'], [1, 4, 's']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 4, 's'], [0, 0, 'n'], [0, 0, 'n'], [2, 4, 'e'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [1, 2, 'o'], [1, 3, 'n'], [1, 1, 'n'], [1, 3, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 5, 'n']]]
    elif mapChoice == 3:#dynasty
        board = [[[2, 5, 's'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [2, 4, 's'], [2, 3, 's'], [2, 4, 'e'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [2, 1, 's'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[2, 4, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [2, 4, 's'], [2, 3, 's'], [2, 4, 'e'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[2, 4, 'e'], [0, 0, 'n'], [2, 2, 's'], [0, 0, 'n'], [1, 4, 'o'], [0, 0, 'n'], [1, 4, 'e'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [2, 4, 'o'], [0, 0, 'n'], [2, 4, 'e'], [0, 0, 'n'], [1, 2, 'n'], [0, 0, 'n'], [1, 4, 'o']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 2, 'e'], [1, 3, 'n'], [1, 4, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 4, 's']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 1, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n']], [[0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 4, 'o'], [1, 3, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [0, 0, 'n'], [1, 5, 'n']]]
    return board


board = loadBoard(1)
print(board)
