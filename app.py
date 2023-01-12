from constants import PLAYERS, TEAMS
from teams import Team

def clean_data(data):
    squeaky = []
    for player in data.copy():
        player['guardians'] = player['guardians'].split(" and ")
        if player['experience'] == "YES":
            player['experience'] = True
        elif player['experience'] == "NO":
            player['experience'] = False
        player['height'] = int(player['height'].split()[0])
        squeaky.append(player)
    return squeaky

def pick_teams(data, players):
    teams = []
    for t in data:
        teams.append(Team(t))
    print(len(teams))
    xp = []
    noob = []
    for player in players:
        if player['experience'] == True:
            xp.append(player)
        else:
            noob.append(player)
    for t in teams:
        xpplayersnum = int(len(xp))
        for i in range(0, int(xpplayersnum / len(teams))):
            print(f'looping; {xp}')
            t.players.append(xp[0])
            del xp[0]
        print(f'finished team : {t.players}')

def counter(players):
    xp = []
    noob = []
    for p in players:
        if p['experience'] == False:
            noob.append(p)
        else:
            xp.append(p)
    print(len(xp))
    print(len(noob))


if __name__ == '__main__':
    wenis = pick_teams(TEAMS, clean_data(PLAYERS))
    print(wenis)
