class Team: 

    def __init__(self, name, position_list, player_list): 
        self.name = name
        self.position_list = position_list
        self.players = dict()
        
        # Empty dictionary to set up a dict of players grouped by position
        for pl in position_list:
            self.players[pl.upper()] = [] 

        # Adds player to the player dict based on their position 
        for p in player_list:
            position = p[0]
            player = p[1]
            if position in self.position_list:
                self.players[position].append(player)