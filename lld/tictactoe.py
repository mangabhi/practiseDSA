class Player:
    def __init__(self,name,marker):
        self.name=name
        self.marker=marker


class Board:
    def __init__(self,size):
        self.size=size

    def reset(self,size):
        self.board=[['' for x in range(size).copy() for y in range(size)]]
        self.rowCounts={}
        self.colCounts={}
        self.dialogCounts={}
        self.size=size

    def place(self,player,x,y):
        marker=player.marker
        if self.board[y][x] != '':
            raise ValueError
        else:
            self.board[y][x]=marker
            self.rowCounts[y] = self.rowCounts.get(y,{})
            self.rowCounts[y][marker]=self.rowCounts[y].get(marker,0)+1

            if self.rowCounts[y][marker] == self.size:
                return True
            self.colCounts[x] = self.colCounts.get(x,{})
            self.colCounts[x][marker]=self.colCounts[x].get(marker,0)+1
            if self.colCounts[x][marker]==self.size:
                return True

            if x==y:
                self.dialogCounts["forwards"]=self.dialogCounts.get("forwards",{})
                self.dialogCounts["forwards"][marker]=self.dialogCounts["forwards"].get(marker,0)+1

                if self.dialogCounts["forwards"][marker]==self.size:
                    return True

            if x+y == self.size-1:
                self.dialogCounts["backwards"]=self.dialogCounts.get("backwards",{})
                self.dialogCounts["backwards"][marker]=self.dialogCounts["backwards"].get(marker,0)+1

                if self.dialogCounts["backwards"][marker]==self.size:
                    return True
            return False
            

class Game:
    def __init__(self,player1,player2,board):
        self.board=board
        self.player1=player1
        self.player2=player2

    def playGame(self):
        currTurn=1
        gameDone=False
        while not gameDone:
            currPlayer=self.player1 if currTurn%2==1 else self.player2
            x=int(input("Write x position of marker"))
            y=int(input("Write y position of marker"))
            if self.board.place(currPlayer,x,y):
                gameDone=True
                print(f"{currPlayer.name} wins!!")
            else:
                currTurn +=1

player1=Player("Big Dick Jordan","x")
player2=Player("small Dick Elon","o") 
board=Board(3)
game=Game(player1,player2,board)
game.playGame() 