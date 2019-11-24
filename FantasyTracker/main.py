import os
import csv
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

    # Class Initialization
    FpScraper = FantasyProsScraper(league_size, positions, rankings)
    Directory = Directory()

    # Create Directories
    Directory.setWeek(week)
    Directory.createWeeklyRankingDirectories()
    
    # Get all Player rankings 
    playerRankings = FpScraper.getData()

    # Write to a CSV file
    # for position in playerRankings:
    #     print("Outputting {} rankings to csv".format(position))
    #     filename = '{}.csv'.format(position)     
    #     with open("{}/{}".format(Directory.getFormattedWeek(),filename), 'w', newline='') as csvfile:
    #         writer = csv.writer(csvfile)
    #         rank = 1
    #         tier = 1
    #         writer.writerow(['Rank', 'Player Name', 'Tier'])
    #         for player in playerRankings[position]:
    #             writer.writerow(player)