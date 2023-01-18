from constants import PLAYERS, TEAMS
from teams import Team
import statistics

class Team:

    def __init__(self, teamname):
        self.name = teamname
        self.number_of_players = 0
        self.number_of_xpplayers = 0
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

    def balance_teams(self, pdata):
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
            t.number_of_xpplayers = xpshare
            t.number_of_noobs = noobshare
            t.number_of_players = xpshare + noobshare
            for _ in range(noobshare):
                t.players.append(noobs[0])
                del noobs[0]
            for _ in range(xpshare):
                t.players.append(xp[0])
                del xp[0]
            avheightlist = []
            for p in t.players:
                avheightlist.append(p['height'])
            t.avgheight = statistics.mean(avheightlist)

    def stat_fmt(self, teamindex):
        print(f'''---------------------------------------------------------
Team Name: {self.teams[teamindex]}
Total Players: {self.teams[teamindex].number_of_players}
Experienced: {self.teams[teamindex].number_of_xpplayers}
Inexperienced: {self.teams[teamindex].number_of_noobs}
Average Height: {statistics.mean([p['height'] for p in self.teams[teamindex].players])}
Player names: {', '.join([p['name'] for p in self.teams[teamindex].players])}
Guardians of Players: {', '.join([', '.join(ptu) for ptu in [p['guardians'] for p in self.teams[teamindex].players]])}''')
        input('Press ENTER to continue...')
        print('''---------------------------------------------------------
My purpose has been served...
Do you want to see the stats again?''')


    def menu(self):
        print('''--------B-A-S-K-E-T-B-A-L-L---S-T-A-T-S---T-O-O-L--------
I am a program and my purpose is to balance teams :)
I have already used your data to fulfill my purpose.
---------------------------------------------------------
Would you like to see what I created for you?''')
        serving = True
        while serving:
            try:
                choice = input('''---------------------------------------------------------
A. See Balanced Teams
B. Quit
---------------------------------------------------------
Enter selection here:   ''').title()
                if choice == 'A':
                    choosy = input(f'''---------------------------------------------------------
What team are you interested in?
---------------------------------------------------------
A. {self.teams[0]}
B. {self.teams[1]}
C. {self.teams[2]}
---------------------------------------------------------
Enter selection here:   ''').title()
                    if choosy == 'A':
                        self.stat_fmt(0)
                    elif choosy == 'B':
                        self.stat_fmt(1)
                    elif choosy == 'C':
                        self.stat_fmt(2)
                    else:
                        raise Exception('''---------------------------------------------------------
Please select only A, B, or C.''')
                elif choice == 'B':
                    print('''---------------------------------------------------------
            It was a pleasure to serve you :)
---------------------------------------------------------''')
                    serving = False
                else:
                    raise TypeError("""---------------------------------------------------------
You must select either A or B. Nothing else is valid.""")
            except Exception as err:
                print(err)


    def run_it(self, pdata, tdata):
        self.teams = self.team_maker(tdata)
        self.balance_teams(pdata.copy())
        self.menu()




if __name__ == '__main__':
    game = Game()
    game.run_it(game.clean_data(PLAYERS), TEAMS)


