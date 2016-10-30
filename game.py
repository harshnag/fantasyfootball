import numpy as np
import random

class Position:
    def __init__(self):
        #attack, defense
        self.HomePlayer = [5, 5]
        self.current0phase = 0
        self.AwayPlayer = [5, 5]
        self.currentAwayphase = 1
        self.inplay = '-'
        return
    
    def __repr__(self):
        return self.inplay #'Home:%sAway:%s' % (self.HomePlayer, self.AwayPlayer)
    
    def __str__(self):
        return 'Home: %s, Away: %s' % (self.HomePlayer, self.AwayPlayer)

class Encounter:
    
    def combat(self, boardposition):
        boardposition.inplay = '*'
        return self.combatb(boardposition.HomePlayer, boardposition.current0phase,
                            boardposition.AwayPlayer, boardposition.currentAwayphase)
    
    def combatb(self, home, current0phase, away, currentAwayphase):
        Homeroll = home[current0phase] * self.roll()
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
        self.rows = 6
        self.cols = 6
        self.homegoals = 0
        self.awaygoals = 0
        self.time = 0
        self.timeincrement = 1
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
        if(self.debug):
            print ('passing to row %s' % passwide)
        if(passwide >= 0 and passwide <= self.rows):
            self.currentrow = passwide

    def homewins(self):
        if(self.debug):
            print ('home wins possession and '
                   'chooses where to attack from %s %s' %
                (self.currentcol, self.currentrow))
        p = self.currentposition()
        p.current0phase = 0
        p.currentAwayphase = 1
        p.inplay = 'h'
        self.juke()
        self.currentcol = self.currentcol - 1
        #self.gameloop()
        return
    
    def awaywins(self):
        if(self.debug):
            print ('away wins possession and '
                   'chooses where to attack from %s %s' %
                (self.currentcol, self.currentrow))
        p = self.currentposition()
        p.current0phase = 1
        p.currentAwayphase = 0
        p.inplay = 'a'
        self.juke()
        self.currentcol = self.currentcol + 1
        #self.gameloop()
        return

    def isgoal(self, expectedside, goalattempt):
        return expectedside == goalattempt

    def scored(self, goals):
        goals = goals + 1
        return
        
    def currentposition(self):
        return self.board[self.currentcol][self.currentrow]

    def scoringposition(self):
        if(self.currentcol >= self.cols):
            print ('away reached byline, attempting to score')
            battle = self.enc.combat(self.board[self.currentcol-1][self.currentrow])
            if(self.isgoal('away', battle)):
                print('***Goal! Scored by away team in minute %s***' % self.time)
                self.awaygoals = self.awaygoals + 1
                self.setkickoffposition()
            else:
                #shot at goal failed
                self.currentcol = self.currentcol - 1
        elif (self.currentcol < 0):
            print ('home reached byline, attempting to score')
            battle = self.enc.combat(self.board[self.currentcol+1][self.currentrow])
            if(self.isgoal('home', battle)):
                print('***Goal! Scored by home team in minute %s***' % self.time)
                self.homegoals = self.homegoals + 1
                self.setkickoffposition()
            else:
                self.currentcol = self.currentcol + 1
                
    def gameloop(self):
        while (self.time < self.timemax):
            self.time = self.time + self.timeincrement
            print('Game time is now %s' % self.time)

            self.scoringposition()
            
            battle = self.enc.combat(self.board[self.currentcol][self.currentrow])
            while self.state is not 'complete':
                #print(battle)
                #print(np.matrix(self.board))
                if(battle == 'home'):
                    self.homewins()
                    break
                elif(battle == 'away'):
                    self.awaywins()
                    break
                else:
                    battle = self.enc.combat(self.board[self.currentcol][self.currentrow])
                        
        print('Time up!')
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
print('Final score\n Home: %s Away: %s' % (g.homegoals, g.awaygoals))
      
      
