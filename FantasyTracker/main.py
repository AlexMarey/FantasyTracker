import os
import json
import sys
from FantasyProsScraper import FantasyProsScraper
from Directory import Directory

if __name__ == "__main__":
    ### LOOK INTO ARGPARSE
    week = int(sys.argv[1])
    ###
    
    # Class Initialization
    FpScraper = FantasyProsScraper()
    Directory = Directory()

    # Create Directories
    Directory.setWeek(week)
    Directory.createWeeklyRankingDirectories()
    
    # Get all Player rankings 
    playerRankings = FpScraper.getData()

    # Store the Data
    for position in ["qb", "rb", "wr", "te", "k", "flex"]:
        Directory.storeData(playerRankings[position],position)
    
    # Import Team/League Settings
    with open('teams/PalmettoLeague.json') as jsonFile:
        leagueSettings = json.load(jsonFile)

    leagueSize = leagueSettings["leagueSize"]
    positions = leagueSettings["positions"]
    players = leagueSettings["players"]
    print("Players from Team: {}".format(players))

    # Compare Data with team 
    for teamPlayer in players:
        position = teamPlayer["position"]
        if (position != 'def'):
            for playerRank in playerRankings[position]:
                if (teamPlayer["name"] == playerRank["name"]):
                    teamPlayer["rank"] = playerRank["rank"]
                    # print("Player Found! {} is {}. Rank: {}".format(teamPlayer["name"],playerRank["name"],playerRank["rank"]))

    # organized by postion, ordered by rank
    # team = sorted(players, key=players.__getitem__)
    
    for teamPlayer in players:
        try:
            print("{}: {} [{}]".format(teamPlayer["position"],teamPlayer["name"],teamPlayer["rank"]))
        except KeyError as key:
            print("{}: {} [{}]".format(teamPlayer["position"],teamPlayer["name"], "Not Found"))    
