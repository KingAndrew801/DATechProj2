from constants import PLAYERS, TEAMS
from teams import Team

class Team:

    def __init__(self, teamname):
        self.name = teamname
        self.number_of_players = 0
        self.number_of_expplayers = 0
        self.number_of_noobs = 0
        self.players = []
        self.avgheight = None

    def __repr__(self):
        return f'{self.name}'

class Game:

    def __init__(self):
        self.teams = []

    def team_maker(self, tdata):
        newteams = []
        for team in tdata:
            newteams.append(Team(team))
        return newteams


    def clean_data(self, pdata):
        squeaky = []
        data = pdata.copy()
        for player in data:
            player['guardians'] = player['guardians'].split(" and ")
            if player['experience'] == "YES":
                player['experience'] = True
            elif player['experience'] == "NO":
                player['experience'] = False
            player['height'] = int(player['height'].split()[0])
            squeaky.append(player)
        return squeaky

    def pick_teams(self, pdata):
        xp = []
        noobs = []
        for p in pdata:
            if p['experience']  == True:
                xp.append(p)
            elif p['experience'] == False:
                noobs.append(p)
        noobshare = int(len(noobs) / len(self.teams))
        xpshare = int(len(xp) / len(self.teams))

        for t in self.teams:
            pindex = 0
            for p in xp:
                print(p)
                rangeindex = 0
                for _ in range(xpshare):
                    print(f'range index: {rangeindex}')
                    rangeindex += 1
                    if p['experience'] == True:
                        print(p)
                        print(xp)
                        t.players.append(xp[pindex])
                        print(f'xp[pindex]: {xp[pindex]}')
                        del xp[pindex]
                        print(f'########### this is self.teams:{t}')
                pindex += 1



    def run_it(self, pdata, tdata):
        self.teams = self.team_maker(tdata)
        self.pick_teams(pdata.copy())




if __name__ == '__main__':
    game = Game()
    game.run_it(game.clean_data(PLAYERS), TEAMS)


