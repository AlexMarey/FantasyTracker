import os
import csv
from FantasyProsScraper import FantasyProsScraper as FpScraper

if __name__ == "__main__":
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
    week_number = 5
    directory = 'rankings/'
    directory_week = FpScraper.set_directory_week(directory, week_number)
    FpScraper.create_weekly_ranking_directories(directory, directory_week)
    
    # Get all Player rankings 
    player_rankings_std = dict()

    print("Time to get the player rankings")
    for p in positions:
        # Standard Scoring
        print("Position: {}".format(p))
        FpScraper.url_rankings_std = FpScraper.make_url(rankings, p)
        print("Url: {}".format(FpScraper.url_rankings_std))
        FpScraper.player_rankings_std[p] = FpScraper.get_players_rankings(FpScraper.url_rankings_std, league_size, p)
        print("Data: {}".format(FpScraper.player_rankings_std[p]))

    # Write to a CSV file
    for position in player_rankings_std:
        print("Outputting {} rankings to csv".format(position))
        filename = '{}.csv'.format(position)     
        with open("{}{}".format(directory_week,filename), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            rank = 1
            tier = 1
            writer.writerow(['Rank', 'Player Name', 'Tier'])
            for player in player_rankings_std[position]:
                writer.writerow(player)
    
    # Find teams to look up rankings for
    if not os.path.exists("./teams"):
        pass
    else:
        pass
