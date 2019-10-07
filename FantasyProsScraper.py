from pathlib import Path
from Scraper import Scraper
from bs4 import BeautifulSoup

class FantasyProsScraper():

    def make_url(purpose, position, scoring='standard'):
        base = 'https://www.fantasypros.com/nfl/'
        if scoring == 'half-point-ppr':
            if purpose == 'projections': 
                # Half PPR & Projections
                return base + '{0}/{1}.php?scoring=HALF'.format(purpose, position)
            # Half PPR & Rankings
            return base + '{0}/{1}-{2}.php'.format(purpose, scoring, position)
        # Standard & Projections or Rankings
        return base + '{0}/{1}.php'.format(purpose, position)


    def get_table_data(url): 
        response = Scraper.simple_get(url)

        if response is not None:
            results = list()
            html = BeautifulSoup(response, 'html.parser')
            table = html.tbody
            table_rows = table.select('tr')

            for row in table_rows:
                col = row.find_all('td')
                col = [ele.text.strip() for ele in col]
                results.append([ele for ele in col if ele])        
            return results

    def parse_names(name_list):
        split_name = name_list.split('. ')
        # Check for names like C.J. Beathard
        if len(split_name) > 2: 
            player_name = '. '.join(split_name[:-1])[:-1]
        else: 
            player_name = split_name[0][:-1]
        return player_name

    def get_players_rankings(url, league_size, position): 
        # Get Data
        data = get_table_data(url)
        # Parse Rankings
        rankings = list()
        tier = 1
        for row in data: 
            #print(row)
            if(len(row) == 7):
                player_name = parse_names(row[1])
                rank = int(row[0])
                tier_rank = '{}{}'.format(position.upper(), str(tier))
                if (rank) % league_size == 0: 
                    tier = tier + 1
                #print([rank, player_name, tier_rank])
                rankings.append([rank, player_name, tier_rank])
        return rankings

    def get_players_projections(url): 
        # Get Data
        data = get_table_data(url)
        # Parse Projections
        # To do implement projections!
        return data

    def set_directory_week(directory, week_number):
        week = 'Week_{}'.format(week_number)
        directory_week = '{}{}/'.format(directory, week)
        return directory_week

    def create_weekly_ranking_directories(directory, directory_week):
        Path(directory).mkdir(parents=True, exist_ok=True)
        Path(directory_week).mkdir(parents=True, exist_ok=True)
        return