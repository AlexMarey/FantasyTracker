import os
import json
from FantasyProsScraper import FantasyProsScraper
from Directory import Directory

if __name__ == "__main__":
    # Variables
    rankings = 'rankings'
    
    # Import Team/League Settings
    with open('teams/PalmettoLeague.json') as jsonFile:
        leagueSettings = json.load(jsonFile)

    week = leagueSettings["currentWeek"]
    leagueSize = leagueSettings["leagueSize"]
    positions = leagueSettings["positions"]
    
    # Class Initialization
    FpScraper = FantasyProsScraper(leagueSize, positions, rankings)
    Directory = Directory()

    # Create Directories
    Directory.setWeek(week)
    Directory.createWeeklyRankingDirectories()
    
    # Get all Player rankings 
    playerRankings = FpScraper.getData()

    # Store the Data
    for position in positions:
        Directory.storeData(playerRankings[position],position)

    # Compare Data with team 