# fantasyfootball

Python version of grid-based soccer game, all of the relevant code is in game.py. Rest of the files exist because I started playing with django, then decided that it would be a good idea to do that separate from the actual game logic engine. That's in my other github project.

Plays itself right now, working on adding player support after finising Django version. Here's a preview of what it looks like if you're too lazy like me to run code from github on your machine. The matrix represents the playing field. The numbers that end up on the field tell the story of who last won possession in each square on the field, the result of a battle between 2 players. 1 means the home team won the midfield battle, 2 means the away team won. 9 represents the current square in play. If a goal is scored, the game restarts at the center (this is why sometimes the field will have multiple 9s, I don't reset the square yet after scoring).

	[[0 0 0 0 0 0 0]
	 [0 0 0 0 0 0 0]
	 [0 0 0 0 0 0 0]
	 [0 0 0 0 0 0 0]
	 [0 0 0 0 0 0 0]
	 [0 0 0 0 0 0 0]]
	Game time is now 1
	Game time is now 2
	Game time is now 3
	Game time is now 4
	Game time is now 5
	Game time is now 6
	Game time is now 7
	Game time is now 8
	Game time is now 9
	Game time is now 10
	Game time is now 11
	Game time is now 12
	Game time is now 13
	home reached byline, attempting to score
	***Goal! Scored by home team in minute 13***
	Game time is now 14
	Game time is now 15
	Game time is now 16
	Game time is now 17
	Game time is now 18
	Game time is now 19
	Game time is now 20
	away reached byline, attempting to score
	***Goal! Scored by away team in minute 20***
	Game time is now 21
	Game time is now 22
	Game time is now 23
	Game time is now 24
	Game time is now 25
	Game time is now 26
	Game time is now 27
	Game time is now 28
	Game time is now 29
	Game time is now 30
	Game time is now 31
	Game time is now 32
	Game time is now 33
	Game time is now 34
	Game time is now 35
	Game time is now 36
	Game time is now 37
	Game time is now 38
	Game time is now 39
	Game time is now 40
	Game time is now 41
	Game time is now 42
Game time is now 43
Game time is now 44
Game time is now 45
Game time is now 46
Game time is now 47
Game time is now 48
Game time is now 49
Game time is now 50
Game time is now 51
Game time is now 52
Game time is now 53
Game time is now 54
Game time is now 55
away reached byline, attempting to score
Game time is now 56
away reached byline, attempting to score
***Goal! Scored by away team in minute 56***
Game time is now 57
Game time is now 58
Game time is now 59
away reached byline, attempting to score
***Goal! Scored by away team in minute 59***
Game time is now 60
Game time is now 61
Game time is now 62
away reached byline, attempting to score
***Goal! Scored by away team in minute 62***
Game time is now 63
Game time is now 64
Game time is now 65
Game time is now 66
Game time is now 67
Game time is now 68
Game time is now 69
Game time is now 70
Game time is now 71
Game time is now 72
Game time is now 73
Game time is now 74
home reached byline, attempting to score
Game time is now 75
home reached byline, attempting to score
Game time is now 76
home reached byline, attempting to score
***Goal! Scored by home team in minute 76***
Game time is now 77
Game time is now 78
Game time is now 79
away reached byline, attempting to score
Game time is now 80
Game time is now 81
Game time is now 82
Game time is now 83
Game time is now 84
Game time is now 85
Game time is now 86
Game time is now 87
home reached byline, attempting to score
Game time is now 88
home reached byline, attempting to score
***Goal! Scored by home team in minute 88***
Game time is now 89
Game time is now 90
Time up!
Final game state:
[[0, 0, 0, 0, 1, 1, 9], [0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 2, 0, 1], [0, 0, 2, 2, 1, 1, 1], [0, 1, 2, 1, 2, 2, 1], [0, 1, 9, 2, 2, 1, 1]]
[[0 0 0 0 1 1 9]
 [0 0 0 0 1 1 1]
 [0 0 0 1 2 0 1]
 [0 0 2 2 1 1 1]
 [0 1 2 1 2 2 1]
 [0 1 9 2 2 1 1]]
Final score
 Home: 3 Away: 4
