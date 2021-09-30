from Scraper import Scraper
from bs4 import BeautifulSoup


class FantasyProsScraper(Scraper):
    def __init__(self):
        self.positions = ["qb", "rb", "wr", "te", "k", "flex"]

    def makeUrl(self, purpose, position, scoring=''):
        BASE_URL = 'https://www.fantasypros.com/nfl/'
        if scoring != '' and position in ['rb', 'wr', 'flex', 'te']:
            return '{0}{1}/{2}-{3}.php'.format(BASE_URL, purpose, scoring, position)
        return '{0}{1}/{2}.php'.format(BASE_URL, purpose, position)
