from Scraper import Scraper
from bs4 import BeautifulSoup

class FantasyProsScraper(Scraper):

    
    def getData(self, leagueSize, positions, purpose):
        playerRankings = dict()
        
        for item in positions:
             print("Position: {}".format(item))
             url = self.makeUrl(purpose, item)
             print("Url: {}".format(url))
             playerRankings[item] = self.getPlayerRankings(url, leagueSize, item)
             print("Data: {}".format(playerRankings[item]))
        return playerRankings
    
    def makeUrl(self, purpose, position, scoring='half-point-ppr'):
        base = 'https://www.fantasypros.com/nfl/'
        if scoring == 'half-point-ppr':
            if purpose == 'projections': 
                # Half PPR & Projections
                return base + '{0}/{1}.php?scoring=HALF'.format(purpose, position)
            # Half PPR & Rankings
            return base + '{0}/{1}-{2}.php'.format(purpose, scoring, position)
        # Standard & Projections or Rankings
        return base + '{0}/{1}.php'.format(purpose, position)

    def getPlayerData(self, url): 
        response = self.simple_get(url)
        
        if response is not None:
            results = list()
            html = BeautifulSoup(response, 'html.parser')
            table = html.tbody
            table_rows = table.select('tr')

            for row in table_rows:
                cell = row.find_all('td')
                cell = [element.text.strip() for element in cell]
                results.append([element for element in cell if element])        
            return results

    def parsePlayerNames(self, name_list):
        split_name = name_list.split('. ')
        # Check for names like C.J. Beathard
        if len(split_name) > 2: 
            player_name = '. '.join(split_name[:-1])[:-1]
        else: 
            player_name = split_name[0][:-1]
        return player_name

    def getPlayerRankings(self, url, league_size, position): 
        # Get Data
        data = self.getPlayerData(url)
        # Parse Rankings
        rankings = list()
        tier = 1
        for row in data: 
            #print(row)
            if(len(row) > 1):
                #print("Calling parsePlayerNames")
                player_name = self.parsePlayerNames(row[1])
                rank = int(row[0])
                tier_rank = '{}{}'.format(position.upper(), str(tier))
                if (rank) % league_size == 0: 
                    tier = tier + 1
                #print([rank, player_name, tier_rank])
                rankings.append([rank, player_name, tier_rank])
        return rankings