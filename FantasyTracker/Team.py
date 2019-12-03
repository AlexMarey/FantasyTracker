

class Team():

    def __init__(self, teamConfig):
        self.leagueSize = teamConfig["leagueSize"]
        self.leagueName = teamConfig["leagueName"]
        self.teamName = teamConfig["teamName"]
        self.positions = teamConfig["positions"]
        self.players = teamConfig["players"]

        self.quarterBacks = list()
        self.runningBacks = list()
        self.wideReceivers = list()
        self.tightEnds = list()
        self.kickers = list()

        self.team = [
            ("Quarter Back", self.quarterBacks), 
            ("Running Back", self.runningBacks), 
            ("Wide Receiver", self.wideReceivers), 
            ("Tight End", self.tightEnds), 
            ("Kicker", self.kickers), 
        ]

    def addPlayer(self, player):
        newPlayer = (player["name"], player["rank"])

        if player["position"] == "qb":
            self.quarterBacks.append(newPlayer)
            return
        if player["position"] == "rb":
            self.runningBacks.append(newPlayer)
            return
        if player["position"] == "wr":
            self.wideReceivers.append(newPlayer)
            return
        if player["position"] == "te":
            self.tightEnds.append(newPlayer)
            return
        if player["position"] == "k":
            self.kickers.append(newPlayer)
            return

    def getPlayerRankings(self, rankings):
        for teamPlayer in self.players:
            position = teamPlayer["position"]
            playerFound = False

            if (position != 'def'):
                for playerRank in rankings[position]:
                    if (teamPlayer["name"] == playerRank["name"]):
                        teamPlayer["rank"] = playerRank["rank"]
                        playerFound = True
            if (not playerFound): 
                teamPlayer["rank"] = "No Rank Available"

            self.addPlayer(teamPlayer)
                
    def printTeam(self):
        team = [
            ("Quarter Back", self.quarterBacks), 
            ("Running Back", self.runningBacks), 
            ("Wide Receiver", self.wideReceivers), 
            ("Tight End", self.tightEnds), 
            ("Kicker", self.kickers), 
        ]
        print("~~~~~~~~~~")
        print(self.teamName)
        print("~~~~~~~~~~")
        for position in team:
            self.printPosition(position[0], position[1])
        return

    def printPosition(self, position, playerList):
        print(position)
        print("~~~~~~~~~~~~~~~~~")
        for player in playerList:
            print("{} - {}".format(player[0], player[1]))
        print('\n')
        return