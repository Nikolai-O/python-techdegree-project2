from constants import PLAYERS
import copy

players_copy = copy.deepcopy(PLAYERS)
Panthers = []
Bandits = []
Warriors = []


def clean_data(const):
    for player in const:
        player['height'] = int(player['height'][0]+player['height'][1])
    for player in const:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    for player in const:
        if len(player['guardians']) == 1:
            player['guardians'] = player['guardians'].split()
        if len(player['guardians']) > 1:
            player['guardians'] = player['guardians'].split(' and ')


def balance_team(const):
    experienced_players = []
    for player in players_copy:
        if player['experience'] == True:
            experienced_players.append(player)

    inexperienced_players = []
    for player in players_copy:
        if player['experience'] == False:
            inexperienced_players.append(player)

    while experienced_players:
            Panthers.append(experienced_players.pop(0))
            Bandits.append(experienced_players.pop(0))
            Warriors.append(experienced_players.pop(0))

    while inexperienced_players:
            Panthers.append(inexperienced_players.pop(0))
            Bandits.append(inexperienced_players.pop(0))
            Warriors.append(inexperienced_players.pop(0))


def experienced(team):
    experienced_players = 0
    for player in team:
        if player['experience'] == True:
            experienced_players += 1
    return experienced_players


def inexperienced(team):
    inexperienced_players = 0
    for player in team:
        if player['experience'] == False:
            inexperienced_players += 1
    return inexperienced_players


def calc_average_height(team):
    total_height = 0
    for player in team:
        total_height += player['height']
    average_height = round(total_height / len(team), 1)
    return average_height


def add_guardians(team):
    guardians = []
    team_copy = copy.deepcopy(team)
    for player in team_copy:
        player['guardians'] = ', '.join(player['guardians'])
    for player in team_copy:
        guardians.append(player['guardians'])
    return ', '.join(guardians)


if __name__ == '__main__':
    clean_data(players_copy)
    balance_team(players_copy)
    selection = 0

    while selection != 2:

        print("BASKETBALL STATISTICS TOOL\n\n"+"-"*11+"MENU"+"-"*11+"\n\n Please enter your selection:\n  1) Display Team Statistics\n  2) Quit\n")

        try:
            selection = int(input("Enter an option > "))
            if selection > 2 or selection < 1:
                print("\n*ERROR* Please enter either 1 or 2 *ERROR*\n")
        except Exception:
            print("\n*ERROR* Please enter a *NUMBER* (either 1 or 2) *ERROR*\n")

        if selection == 1:
            print("\n1) Panthers\n2) Bandits\n3) Warriors\n")
            team_selection = 0
            while not team_selection:

                try:
                    team_selection = int(input("Enter an option > "))
                    if team_selection > 3 or team_selection < 1:
                        print("\n*ERROR* Please enter either 1, 2 or 3 *ERROR*\n")
                        team_selection = 0
                except Exception:
                    print("\n*ERROR* Please enter a *NUMBER* (either 1, 2 or 3) *ERROR*\n")
                    team_selection = 0
                if team_selection == 1:
                    experienced_players = experienced(Panthers)
                    inexperienced_players = inexperienced(Panthers)
                    average_height = calc_average_height(Panthers)
                    guardians_list = add_guardians(Panthers)

                    print("""\nTeam: Panthers
--------------------\n
Total players: {}
Experienced players: {}
Inexperienced players: {}
Average height: {}\n
Players on team:""".format(len(Panthers), format(experienced_players), format(inexperienced_players), format(average_height)))
                    panthers_players = []
                    for player in Panthers:
                        panthers_players.append(str(player['name']))
                    print(f"  {panthers_players[0]}, {panthers_players[1]}, {panthers_players[2]}, {panthers_players[3]}, {panthers_players[4]}, {panthers_players[5]}\n")
                    print("Guardians:\n  {}\n".format(guardians_list))
                    input("Press ENTER to continue... \n")

                elif team_selection == 2:
                    experienced_players = experienced(Bandits)
                    inexperienced_players = inexperienced(Bandits)
                    average_height = calc_average_height(Bandits)
                    guardians_list = add_guardians(Bandits)

                    print("""\nTeam: Bandits
--------------------\n
Total players: {}
Experienced players: {}
Inexperienced players: {}
Average height: {}\n
Players on team:""".format(len(Bandits), format(experienced_players), format(inexperienced_players), format(average_height)))
                    bandits_players = []
                    for player in Bandits:
                        bandits_players.append(str(player['name']))
                    print(f"  {bandits_players[0]}, {bandits_players[1]}, {bandits_players[2]}, {bandits_players[3]}, {bandits_players[4]}, {bandits_players[5]}\n")
                    print("Guardians:\n  {}\n".format(guardians_list))
                    input("Press ENTER to continue... \n")

                elif team_selection == 3:
                    experienced_players = experienced(Warriors)
                    inexperienced_players = inexperienced(Warriors)
                    average_height = calc_average_height(Warriors)
                    guardians_list = add_guardians(Warriors)

                    print("""\nTeam: Warriors
--------------------\n
Total players: {}
Experienced players: {}
Inexperienced players: {}
Average height: {}\n
Players on team:""".format(len(Warriors), format(experienced_players), format(inexperienced_players), format(average_height)))
                    warriors_players = []
                    for player in Warriors:
                        warriors_players.append(str(player['name']))
                    print(f"  {warriors_players[0]}, {warriors_players[1]}, {warriors_players[2]}, {warriors_players[3]}, {warriors_players[4]}, {warriors_players[5]}\n")
                    print("Guardians:\n  {}\n".format(guardians_list))

                    input("Press ENTER to continue... \n")

    print("\nThank you for using BASKETBALL STATISTICS TOOL\n")

