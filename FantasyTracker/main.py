import os
import csv
from FantasyProsScraper import FantasyProsScraper
from Directory import Directory

if __name__ == "__main__":
    FpScraper = FantasyProsScraper()
    Directory = Directory()

    # Variables
    rankings = 'rankings'
    projections = 'projections'
    # halfPPR = 'half-point-ppr'
    qb = 'qb'
    rb = 'rb' 
    wr = 'wr'
    flex = 'flex'
    k = 'k'
    # Removed flex for the time being
    positions = [qb, rb, wr, flex, k]
    league_size = 8
    week = 13
    
    # Create Directories
    Directory.setWeek(week)
    Directory.createWeeklyRankingDirectories()
    
    # Get all Player rankings 
    playerRankings = dict()

    print("Time to get the player rankings")
    for p in positions:
        # Standard Scoring
        print("Position: {}".format(p))
        url_rankings_std = FpScraper.makeUrl(rankings, p)
        print("Url: {}".format(url_rankings_std))
        playerRankings[p] = FpScraper.getPlayerRankings(url_rankings_std, league_size, p)
        print("Data: {}".format(playerRankings[p]))

    # Write to a CSV file
    for position in playerRankings:
        print("Outputting {} rankings to csv".format(position))
        filename = '{}.csv'.format(position)     
        with open("{}/{}".format(Directory.getFormattedWeek(),filename), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            rank = 1
            tier = 1
            writer.writerow(['Rank', 'Player Name', 'Tier'])
            for player in playerRankings[position]:
                writer.writerow(player)