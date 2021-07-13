from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()

teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()

print('This is the input for making teams')
print()
print(players)
print(teamNames)
print()

teamA = []
teamAname = []
teamB = []
teamBname = []
teamC = []
teamCname = []

while len(teamNames) > 3:
  
  teamAnames = (choice(teamNames))
  teamAname.append(teamAnames)
  teamNames.remove(teamAnames)
  
  teamBnames = (choice(teamNames))
  teamBname.append(teamBnames)
  teamNames.remove(teamBnames)
  
  teamCnames = (choice(teamNames))
  teamCname.append(teamCnames)
  teamNames.remove(teamCnames)

while len(players) > 0:
  
  playerA = (choice(players))
  teamA.append(playerA)
  players.remove(playerA)
  
  if players == []:
    break
  
  playerB = (choice(players))
  teamB.append(playerB)
  players.remove(playerB)
  
  if players == []:
    break
  
  playerC = (choice(players))
  teamC.append(playerC)
  players.remove(playerC)

print('Here are your teams:')
print()
print(teamAname, teamA)
print(teamBname, teamB)
print(teamCname, teamC)