import os
from FantasyProsScraper import FantasyProsScraper
from Directory import Directory

if __name__ == "__main__":
    # Variables
    rankings = 'rankings'
    projections = 'projections'
    # halfPPR = 'half-point-ppr'
    qb = 'qb'
    rb = 'rb' 
    wr = 'wr'
    flex = 'flex'
    te = 'te'
    k = 'k'
    # Removed flex for the time being
    positions = [qb, rb, wr, te, flex, k]
    league_size = 8
    week = 12
    
    # Import Team/League Settings

    # Class Initialization
    FpScraper = FantasyProsScraper(league_size, positions, rankings)
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