import os
import json
import sys
from FantasyProsScraper import FantasyProsScraper
from Directory import Directory
from Team import Team

if __name__ == "__main__":
    ### LOOK INTO ARGPARSE
    # week = int(sys.argv[1])
    ###
    
    # Class Initialization
    FpScraper = FantasyProsScraper()
    # Directory = Directory()

    # Create Directories
    # Directory.setWeek(week)
    # Directory.createWeeklyRankingDirectories()
    
    # Get all Player rankings 
    playerRankings = FpScraper.getData()

    # Store the Data
    # for position in ["qb", "rb", "wr", "te", "k", "flex"]:
    #     Directory.storeData(playerRankings[position],position)
    
    # Import Team/League Settings
    leagues = list()
    teamDir = "teams"
    for filename in os.listdir(teamDir):
        path = "{}/{}".format(teamDir, filename)
        with open(path) as jsonFile:
            leagues.append(json.load(jsonFile))


    for teamConfig in leagues:

        team = Team(teamConfig)

        # Compare Data with team 
        team.getPlayerRankings(playerRankings)

        team.printTeam()