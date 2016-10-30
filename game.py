import numpy as np
import random

class Position:
    def __init__(self):
        #attack, defense
        self.OPlayer = [3, 3]
        self.XPlayer = [6, 6]
        self.inplay = 'x'
        return
    
    def __repr__(self):
        return self.inplay #'O:%sX:%s' % (self.OPlayer, self.XPlayer)
    
    def __str__(self):
        return 'O: %s, X: %s' % (self.OPlayer, self.XPlayer)

class Encounter:
    
    def combat(self, board):
        board.inplay = 'o'
        return self.combatb(board.OPlayer, board.XPlayer)
    
    def combatb(self, offense, defense):
        Oroll = offense[0] * self.roll()
        Xroll = defense[1] * self.roll()
        if Oroll > Xroll:
            return 'offense'
        elif Oroll < Xroll:
            return 'defense'
        else:
            return 'pass'
        
    def roll(self):
        return random.randint(1,10)

class Game:
    def __init__(self):
        self.enc = Encounter()
        self.state = 'start'
        self.rows = 3
        self.cols = 3
        self.board = []
        self.drawboard()

    def drawboard(self):
        #Generate rows with length of 4
        for row in range(self.rows):
          # Appen a blank list to each row cell
          self.board.append([Position()])
          for column in range(self.cols):
            # Assign x to each row
            self.board[row].append(Position())
    
    
    def gameloop(self):
        #start in midfield position 2,1
        #[[x x x x]
        #[x x o x]
        #[x x x x]]
        row = 2
        col = 1
        battle = self.enc.combat(self.board[col][row])
        while self.state is not 'complete':
            print(battle)
            print(np.matrix(self.board))
            if(col > self.cols or col < 0):
                print ('col max encountered')
                break
            elif(battle == 'offense'):
                col = col + 1
                battle = self.enc.combat(self.board[col][row])
            elif(battle == 'defense'):
                col = col - 1
                battle = self.enc.combat(self.board[col][row])
            else:
                battle = self.enc.combat(self.board[col][row])

        return
        


g = Game()



#print (board)
print(np.matrix(g.board))
#enc = Encounter()
#print(enc.combat(board[2][1]))


g.gameloop()

#print (board)
print('Final game state:')
print(np.matrix(g.board))
