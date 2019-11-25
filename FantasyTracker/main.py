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
    
    # Compare Data with team 