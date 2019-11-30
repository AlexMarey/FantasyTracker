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
    with open('teams/PalmettoLeague.json') as jsonFile:
        leagueSettings = json.load(jsonFile)

    leagueSize = leagueSettings["leagueSize"]
    positions = leagueSettings["positions"]
    players = leagueSettings["players"]

    team = Team("Palmetto League")

    # Compare Data with team 
    for teamPlayer in players:
        position = teamPlayer["position"]
        playerFound = False

        if (position != 'def'):
            for playerRank in playerRankings[position]:
                if (teamPlayer["name"] == playerRank["name"]):
                    teamPlayer["rank"] = playerRank["rank"]
                    playerFound = True
        if (not playerFound): 
            teamPlayer["rank"] = "No Rank Available"

        team.addPlayer(teamPlayer)
 
    team.printTeam()