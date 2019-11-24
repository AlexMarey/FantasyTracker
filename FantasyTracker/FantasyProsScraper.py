from Scraper import Scraper
from bs4 import BeautifulSoup

class FantasyProsScraper(Scraper):

    def __init__(self, leagueSize, positions, purpose):
        self.leagueSize = leagueSize
        self.positions = positions
        self.purpose = purpose
    
    def getData(self):
        playerRankings = {}
        playerData = list()
        
        for item in self.positions:
            url = self.makeUrl(self.purpose, item)
            playerData = self.getPlayerData(url)
            playerRankings[item] = self.processPayerData(playerData, item)
            # print("Position: {}".format(item))
            # print("Url: {}".format(url))
            print("Data: {}".format(playerRankings[item]))
        return playerRankings
    
    def makeUrl(self, purpose, position, scoring='half-point-ppr'):
        base = 'https://www.fantasypros.com/nfl/'
        if scoring == 'half-point-ppr' and position in ['rb', 'wr', 'flex', 'te']:
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
            

    def processPayerData(self, data, position):
        nameLocation = 1
        rankLocation = 0
        
        processedData = list()
        tier = 1
        
        for item in data:
            if(len(item) > 1):
                
                rank = int(item[rankLocation])
                playerName = self.parsePlayerName(item[nameLocation])
                tierRank = '{}{}'.format(position.upper(), str(tier))
                
                if (rank) % self.leagueSize == 0: 
                    tier = tier + 1
                
                processedData.append({
                    "name": playerName,
                    "rank": rank,
                    "tier": tierRank
                })
        return processedData
    
    def parsePlayerName(self, name_list):
        split_name = name_list.split('. ')
        # Check for names like C.J. Beathard
        if len(split_name) > 2: 
            player_name = '. '.join(split_name[:-1])[:-1]
        else: 
            player_name = split_name[0][:-1]
        return player_name