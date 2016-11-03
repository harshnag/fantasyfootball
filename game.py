import numpy as np
import random

class Position:
    def __init__(self):
        #attack, defense
        self.HomePlayer = [5, 5]
        self.currentHomephase = 0
        self.AwayPlayer = [5, 5]
        self.currentAwayphase = 1
        self.inplay = '0'
        return
    
    def __repr__(self):
        return self.inplay #'Home:%sAway:%s' % (self.HomePlayer, self.AwayPlayer)
    
    def __str__(self):
        return 'Home: %s, Away: %s' % (self.HomePlayer, self.AwayPlayer)

class Encounter:
    
    def combat(self, boardposition):     
        return self.combatb(boardposition.HomePlayer, boardposition.currentHomephase,
                            boardposition.AwayPlayer, boardposition.currentAwayphase)
    
    def combatb(self, home, currentHomephase, away, currentAwayphase):
        Homeroll = home[currentHomephase] * self.roll()
        Awayroll = away[currentAwayphase] * self.roll()
        if Homeroll > Awayroll:
            return 'home'
        elif Homeroll < Awayroll:
            return 'away'
        else:
            return 'no-one'
        
    def roll(self):
        return random.randint(1,10)

class Game:
    def __init__(self):
        self.debug = 0
        self.enc = Encounter()
        self.state = 'start'
        self.rows = 3
        self.cols = 4
        self.homegoals = 0
        self.awaygoals = 0
        self.time = 0
        self.timeincrement = 5
        self.timemax = 90
        self.board = []
        self.setkickoffposition()
        self.drawboard()

    def setkickoffposition(self):
        #start in midfield position 2,1
        #[[x x x x]
        #[x x o x]
        #[x x x x]]       
        self.currentrow = int(self.rows/2)
        self.currentcol = int(self.cols/2)
        
    def drawboard(self):
        #Generate rows with specified length
        for row in range(self.rows):
          # Append a blank list to each row cell
          self.board.append([])
          for column in range(self.cols):
            # Assign Position to each row
            self.board[row].append(Position())

    def juke(self):
        lateral = random.randint(-1,1)
        passwide = self.currentcol + lateral
        if(self.debug):
            print ('lateral passing to col %s' % passwide)
        if(passwide >= 0 and passwide < self.cols):
            self.currentcol = passwide

    def homewins(self):
        if(self.debug):
            print ('home wins possession and '
                   'chooses where to attack from %s %s' %
                (self.currentrow, self.currentcol))
        p = self.currentposition()
        p.currentHomephase = 0
        p.currentAwayphase = 1
        p.inplay = '1'
        self.juke()
        self.currentrow = self.currentrow - 1
        #self.gameloop()
        return
    
    def awaywins(self):
        if(self.debug):
            print ('away wins possession and '
                   'chooses where to attack from %s %s' %
                (self.currentrow, self.currentcol))
        p = self.currentposition()
        p.currentHomephase = 1
        p.currentAwayphase = 0
        p.inplay = '2'
        self.juke()
        self.currentrow = self.currentrow + 1
        #self.gameloop()
        return

    def isgoal(self, expectedside, goalattempt):
        return expectedside == goalattempt

    def scored(self, goals):
        goals = goals + 1
        return
        
    def currentposition(self):
        return self.board[self.currentrow][self.currentcol]

    def scoringposition(self):
        if(self.currentrow >= self.rows):
            print ('away reached byline, attempting to score')
            battle = self.enc.combat(self.board[self.currentrow-1][self.currentcol])
            if(self.isgoal('away', battle)):
                print('***Goal! Scored by away team in minute %s***' % self.time)
                self.awaygoals = self.awaygoals + 1
                self.setkickoffposition()
            else:
                #shot at goal failed
                print ('away failed to score, going back one')
                self.currentrow = self.currentrow - 1
        elif (self.currentrow < 0):
            print ('home reached byline, attempting to score')
            battle = self.enc.combat(self.board[self.currentrow+1][self.currentcol])
            if(self.isgoal('home', battle)):
                print('***Goal! Scored by home team in minute %s***' % self.time)
                self.homegoals = self.homegoals + 1
                self.setkickoffposition()
            else:
                print ('home failed to score, going back one')
                self.currentrow = self.currentrow + 1
                
    def gameloop(self):
        while (self.time < self.timemax):
            print('Game time is now %s' % self.time)
            self.scoringposition()
            battle = self.enc.combat(self.board[self.currentrow][self.currentcol])
            while self.state is not 'complete':
                if(battle == 'home'):
                    self.homewins()
                    break
                elif(battle == 'away'):
                    self.awaywins()
                    break
                else:
                    battle = self.enc.combat(self.board[self.currentrow][self.currentcol])
            self.time = self.time + self.timeincrement
            
        print('Time up!')
        return

g = Game()



#print (board)
print(np.matrix(g.board))
#enc = Encounter()
#print(enc.combat(board[2][1]))


g.gameloop()


print('Final game state:')
print(g.board)
print(np.matrix(g.board))
print('Final score\n Home: %s Away: %s' % (g.homegoals, g.awaygoals))
      
      
