import numpy as np
import random

class Position:
    def __init__(self):
        #attack, defense
        self.OPlayer = [5, 5]
        self.current0phase = 0
        self.XPlayer = [5, 5]
        self.currentXphase = 1
        self.inplay = '-'
        return
    
    def __repr__(self):
        return self.inplay #'O:%sX:%s' % (self.OPlayer, self.XPlayer)
    
    def __str__(self):
        return 'O: %s, X: %s' % (self.OPlayer, self.XPlayer)

class Encounter:
    
    def combat(self, boardposition):
        boardposition.inplay = '*'
        return self.combatb(boardposition.OPlayer, boardposition.current0phase,
                            boardposition.XPlayer, boardposition.currentXphase)
    
    def combatb(self, offense, current0phase, defense, currentXphase):
        Oroll = offense[current0phase] * self.roll()
        Xroll = defense[currentXphase] * self.roll()
        if Oroll > Xroll:
            return 'offense'
        elif Oroll < Xroll:
            return 'defense'
        else:
            return 'no-one'
        
    def roll(self):
        return random.randint(1,10)

class Game:
    def __init__(self):
        self.enc = Encounter()
        self.state = 'start'
        self.rows = 6
        self.cols = 6
        self.board = []
        
        #start in midfield position 2,1
        #[[x x x x]
        #[x x o x]
        #[x x x x]]       
        self.currentrow = 3
        self.currentcol = 3
        
        self.drawboard()

    def drawboard(self):
        #Generate rows with length of 4
        for row in range(self.rows):
          # Appen a blank list to each row cell
          self.board.append([Position()])
          for column in range(self.cols):
            # Assign x to each row
            self.board[row].append(Position())

    def juke(self):
        lateral = random.randint(-1,1)
        passwide = self.currentrow + lateral
        print ('passing to row %s' % passwide)
        if(passwide >= 0 and passwide < self.rows):
            self.currentrow = passwide

    def offensewins(self):
        print ('offense wins possession and '
               'chooses where to attack from %s %s' %
            (self.currentcol, self.currentrow))
        p = self.currentposition()
        p.current0phase = 0
        p.currentXphase = 1
        p.inplay = 'x'
        self.juke()
        self.currentcol = self.currentcol - 1
        self.gameloop()
        return
    
    def defensewins(self):
        print ('defense wins possession and '
               'chooses where to attack from %s %s' %
            (self.currentcol, self.currentrow))
        p = self.currentposition()
        p.current0phase = 1
        p.currentXphase = 0
        p.inplay = 'o'
        self.juke()
        self.currentcol = self.currentcol + 1
        self.gameloop()
        return

    def currentposition(self):
        return self.board[self.currentcol][self.currentrow]
    
    def gameloop(self):
        if(self.currentcol >= self.cols or self.currentcol < 0):
            print ('col max encountered, implement goal')
            return        

        battle = self.enc.combat(self.board[self.currentcol][self.currentrow])
        while self.state is not 'complete':
            print(battle)
            print(np.matrix(self.board))
            if(battle == 'offense'):
                self.offensewins()
                break
            elif(battle == 'defense'):
                self.defensewins()
                break
            else:
                battle = self.enc.combat(self.board[self.currentcol][self.currentrow])        
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
