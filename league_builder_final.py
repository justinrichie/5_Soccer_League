# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

if __name__ == "__main__": #prevent code from being executed when imported
    
    exp = []  # a list where experienced players will be stored
    not_exp = [] # a list where inexperienced players will be stored

    sharks = []
    dragons = []
    raptors = []
    league = [sharks, dragons, raptors]
    team_names = ['Sharks', 'Dragons', 'Raptors']
    dates = ['the 17th \nof March at 3pm',
             'the 17th \nof March at 1pm',
             'the 18th \nof March at 3pm']

    with open('soccer_players.csv') as file:
        player_reader = csv.reader(file)
        all_players = list(player_reader)
        file.close()
        
    for i in all_players[1:]:  # Starting at index 1 as index 0 is not a player
        if i[2] == 'YES':  # Sorting all players into experienced and not_experienced
            exp.append(i)
        else:
            not_exp.append(i)

    exp_per_team = int(len(exp)/3) # How many experienced players will be on each team
    not_exp_per_team = int(len(not_exp)/3) # How many inexperienced players will be on each team

    for team in league:
        for i in exp[:exp_per_team]:
            team.append(i)
            exp.remove(i)

    for team in league:
        for i in not_exp[:not_exp_per_team]:
            team.append(i)
            not_exp.remove(i)
    
def write_letter(list_of_teams, dates, team_names):

    
    for team in list_of_teams:
        if team == sharks:
            team_name = team_names[0]
            date = dates[0]
        elif team == dragons:
            team_name = team_names[1]
            date = dates[1]
        else:
            team_name = team_names[2]
            date = dates[2]        
        for player in team:
            with open('letters2/{}_{}.txt'.format(player[0].split()[0].lower(),
                                     player[0].split()[1].lower()), 'w') as letter:
                letter.write("""Dear {},\n\n You child, {}will be playing soccer as part of the {} team. {}
will get to know all teammates and improve their soccer skills.
Because of this, the first practice day will be on {}. 
Thanks from your commissioner,
Justin Richie""".format(
    player[3], # Name of guardian(s)
    player[0], # player's name
    team_name,      # team name
    player[0].split()[0],  #player's first name
    date)) # the first practice date
                letter.close()


write_letter(league, dates, team_names)
