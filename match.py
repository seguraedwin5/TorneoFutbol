from itertools import combinations

class match():
    def __init__(self, team_list: list):
        self.teams = team_list
        self.victories = {team: 0 for team in self.teams}
        
    def get_teams(self):
        return self.teams
    
    def get_victories(self):
        return self.victories
    
    def get_match_teams_combinations(self):
        return list(combinations(self.get_teams(), 2))
    
    def set_victory(self, team, unit=1):
        self.victories[team] += unit
        
    def reload_victories(self):
        self.victories = {team: 0 for team in self.teams}
        
    def add_team(self, equipo):
        self.teams.append(equipo)