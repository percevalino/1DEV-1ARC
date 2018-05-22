#Numéros pions :
#1 : Pharaoh
#2 : Scarab
#3 : Anubis
#4 : Pyramid
#5 : Sphinx


#Variables :
#board : plateau
#player : joueur qui joue
#i : ligne où va le pion
#j : colonne ou va le pion
#y : ligne où est le pion
#x : colonne où est le pion
#orientation : orientation du pion


#disposition case :
#[1 ou 2 selon joueur, numéro du type de pion, orientation du pion, 1 ou 0 si laser ou non]


def newBoard():
    board = []
    for i in range(8):
        board.append([])
        for j in range(10):
            board[i].append([0, 0, "n", 0])
    return board


def possible(board,player,x,y,i,j):#à vérifier
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
        board[y-1][x-1] = [0, 0, "n", 0]


def win(board,player):# à vérifier
    for i in range(8):
        for j in range(10):
            if board[i][j][1] == 1:
                if board[i][j][0] != player:
                    return False
    return True


#def rotation(board,plzyer,i,j,orientation)



#def laser(?)

board = newBoard()
print(board)
print("\n\n\n")
board[0][0][0] = 1
board[0][0][1] = 4
print(board[0][0])
