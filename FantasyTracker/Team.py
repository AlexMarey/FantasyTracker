

class Team():
    name = None

    quarterBacks = []
    runningBacks = []
    wideReceivers = []
    tightEnds = []
    kickers = []

    team = [
        ("Quarter Back", quarterBacks), 
        ("Running Back", runningBacks), 
        ("Wide Receiver", wideReceivers), 
        ("Tight End", tightEnds), 
        ("Kicker", kickers), 
    ]

    def __init__(self, name):
        self.name = name

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
                
    def printTeam(self):
        team = [
            ("Quarter Back", self.quarterBacks), 
            ("Running Back", self.runningBacks), 
            ("Wide Receiver", self.wideReceivers), 
            ("Tight End", self.tightEnds), 
            ("Kicker", self.kickers), 
        ]
        for position in team:
            self.printPosition(position[0], position[1])
        return

    def printPosition(self, position, playerList):
        print(position)
        print("~~~~~~~~~~~~~~~~~~~~~")
        for player in playerList:
            print("{} - {}".format(player[0], player[1]))
        print('\n')
        return