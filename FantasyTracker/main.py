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
    
    # Create Directories
    Directory.setWeek(11)
    Directory.createWeeklyRankingDirectories()
    
    # Get all Player rankings 
    player_rankings_std = dict()

    print("Time to get the player rankings")
    for p in positions:
        # Standard Scoring
        print("Position: {}".format(p))
        url_rankings_std = FpScraper.make_url(rankings, p)
        print("Url: {}".format(url_rankings_std))
        player_rankings_std[p] = FpScraper.get_players_rankings(url_rankings_std, league_size, p)
        print("Data: {}".format(player_rankings_std[p]))

    # Write to a CSV file
    # for position in player_rankings_std:
    #     print("Outputting {} rankings to csv".format(position))
    #     filename = '{}.csv'.format(position)     
    #     with open("{}{}".format(directory_week,filename), 'w', newline='') as csvfile:
    #         writer = csv.writer(csvfile)
    #         rank = 1
    #         tier = 1
    #         writer.writerow(['Rank', 'Player Name', 'Tier'])
    #         for player in player_rankings_std[position]:
    #             writer.writerow(player)
    
    # Find teams to look up rankings for
    # if not os.path.exists("./teams"):
    #     pass
    # else:
    #     pass
