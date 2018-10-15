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
    
    # Setting up URLs to pull data from 
    # fp -> FantasyPros

    # Rankings || Projections
    rankings = 'rankings'
    projections = 'projections'
    # Scoring
    halfPPR = 'half-point-ppr'
    # Positions
    qb = 'qb'
    rb = 'rb' 
    wr = 'wr'
    flex = 'flex'
    k = 'k'
    positions = [qb, rb, wr, flex, k]

    league_size = 8
    
    # Get all Player rankings for both scoring options
    player_rankings_std = dict()
    player_rankings_half = dict()
    rank = 0
    tier = 1
    for p in positions:
        # Standard Scoring
        url_rankings_std = make_url(rankings, p)
        ranking_list = get_players_rankings(url_rankings_std)
        # Think about how to format the dict so that we can write it to a csv file 
        player_rankings_std[p] = [ranking_list[rank], rank, p.upper() + tier]
        rank = rank + 1
        if rank % league_size == 0:
            tier = tier + 1
        
        # Half - PPR stuff
        #if p is qb or p is k: 
        #    player_rankings_half[p] = player_rankings_std[p]
        #else:
        #    url_rankings_half = make_url(rankings, p, halfPPR)
        #    player_rankings_half[p] = get_players_rankings(url_rankings_half)
        
    # Get players projections
    player_projections_std = dict()
    player_projections_half = dict()
    for p in positions:
        # Standard Scoring
        url_projections_std = make_url(projections, p)
        player_projections_std[p] = get_players_projections(url_projections_std)
        # Half - PPR stuff
        #if p is qb or p is k: 
        #    player_projections_half[p] = player_projections_std[p]
        #else:
        #    url_projections_half = make_url(projections, p, halfPPR)
        #    player_projections_half[p] = get_players_projections(url_projections_half)
        
    # Example dict writer for csv
    #with open('rankings.csv', 'w', newline='') as csvfile:
    #    fieldnames = ['Name', 'Postion', 'Rank']
    #    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #    writer.writeheader()
    #    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    #    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
