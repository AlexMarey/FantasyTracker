# Scrape data from fantasypros using bs4, uses yahoo fantasy api to grab team data, email with smtplib

import os
import csv
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content of the url by making an HTTP GET request. 
    If the content-type of response is some kind of HTML/XML, 
    return the text content, otherwise it returns None
    """
    try:
        with closing(get(url, stream=True)) as resp: 
            if is_good_response(resp):
                return resp.content
            else: 
                return None
    except RequestException as e: 
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response is HTML.
    Returns false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e): 
    """
    Prints error messages.
    """
    print(e)


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


def get_players_rankings(url): 
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        table = html.tbody
        player_html = set()
        player_rankings = set() 

        player_html = table.select('span.short-name')

        for p in player_html:
            player_rankings.add(p.string)

    return list(player_rankings)


def get_players_projections(url): 
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        table = html.tbody
        projection_dict = dict()
        table_rows = table.select('tr')

        for row in table_rows:
            name = row.td.contents[0].string
            proj = row.select('td')[10].string
            projection_dict[name] = proj
            
            return projection_dict


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
    positions = [qb, rb, wr, flex, k]
    league_size = 8
    
    # Get all Player rankings for both scoring options
    player_rankings_std = dict()
    # player_rankings_half = dict()
    print("Time to get the player rankings")
    for p in positions:
        # Standard Scoring
        print("Position: {}".format(p))
        url_rankings_std = make_url(rankings, p)
        print("Url: {}".format(url_rankings_std))
        player_rankings_std[p] = get_players_rankings(url_rankings_std)
        print("Data: {}".format(player_rankings_std[p]))
        # Half - PPR stuff
        #if p is qb or p is k: 
        #    player_rankings_half[p] = player_rankings_std[p]
        #else:
        #    url_rankings_half = make_url(rankings, p, halfPPR)
        #    player_rankings_half[p] = get_players_rankings(url_rankings_half)
        
    # Get players projections
    #player_projections_std = dict()
    #player_projections_half = dict()
    #for p in positions:
        # Standard Scoring
        #url_projections_std = make_url(projections, p)
        #player_projections_std[p] = get_players_projections(url_projections_std)
        # Half - PPR stuff
        #if p is qb or p is k: 
        #    player_projections_half[p] = player_projections_std[p]
        #else:
        #    url_projections_half = make_url(projections, p, halfPPR)
        #    player_projections_half[p] = get_players_projections(url_projections_half)

    # Write to a CSV file
    for position in player_rankings_std:
        print("Outputting {} rankings to csv".format(position))
        filename = '{}.csv'.format(position)    
        directory = 'rankings\\{}'.format(filename)
        with open(directory, 'w', newline='') as csvfile:
            #fieldnames = ['Rank', 'Name', 'Position', 'Tier']
            writer = csv.writer(csvfile)
            rank = 1
            tier = 1
            writer.writerow(['Rank', 'Player Name', 'Tier'])
            for player in player_rankings_std[position]:
                writer.writerow([rank, player, position.upper() + str(tier)])
                rank = rank + 1
                if rank % league_size == 1: 
                    tier = tier + 1
