import argparse


# First task
def medals(filename, country, year, output):
    gold = 0
    silver = 0
    bronze = 0

    res_list = ''
    res = ''

    i = 0

    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if not line: break

            # Split data by information
            info = line.split('\t')
            _name = info[1]
            _team = info[6]
            _noc = info[7]
            _year = info[9]
            _sport = info[12]
            _medal = info[14]
            #if year not in file: print('Invalid year')
            #elif country not in file: print('Invalid country')
            if year == _year:
                if country == _noc or country == _team:
                    if _medal != 'NA\n':
                        list = (f'{_name}-{_sport}-{_medal}')
                        # Count total medals
                        if _medal == 'Gold\n': gold += 1
                        if _medal == 'Silver\n': silver += 1
                        if _medal == 'Bronze\n': bronze += 1

                        total_medals = (f'Total medals: Gold - {gold}, Silver - {silver}, Bronze - {bronze}')
                        # Add result to list
                        res = res + res_list.join(list)
                        i += 1

                        # Print result
                        if i == 10:
                            print(res)
                            print(total_medals)
                            break
        if output == True:
            with open('result.txt', 'w') as file:
                file.write(res)
                file.write(total_medals)


# Second task
def total(filename, year):
    with open(filename, "r") as file:
        # Creating a dictionary that stores medals for each country
        C_M = {}
        while True:
            line = file.readline()
            if not line: break

            # Split data by information
            info = line.split('\t')
            _team = info[6]
            _noc = info[7]
            _year = info[9]
            _medal = info[14]
            if year == _year:
                # check if country already exists in dict
                if _team not in C_M:
                    C_M[_team] = [0, 0, 0]
                if _medal != 'NA\n':
                    # Count total medals
                    if _medal == 'Gold\n': C_M[_team][0] += 1
                    if _medal == 'Silver\n': C_M[_team][1] += 1
                    if _medal == 'Bronze\n': C_M[_team][2] += 1
    for country in C_M:
        total = C_M[country][0] + C_M[country][1] + C_M[country][2]
        if total < 1:
            continue
        else:
            print(f"{country} has total {total} medals: {C_M[country][0]} Gold, {C_M[country][1]} Silver, {C_M[country][2]}")


# Third task
def overall(filename, countries):
    with open(filename, 'r') as file:
        medals_by_year = {}

        for country in countries:
            while True:
                line = file.readline()
                if not line:
                    break

                # Split data by information
                info = line.strip().split('\t')
                _team = info[6]
                _noc = info[7]
                _year = info[9]
                _medal = info[14]

                if _team == country:
                    if _medal != "NA":
                        #Add 1 medal to year if we have key
                        if _year in medals_by_year:
                            medals_by_year[_year] = medals_by_year[_year] + 1
                        #If we don`t have key - create it and add 1 medal
                        else:
                            medals_by_year[_year] = 0
            #Find in each year was maximum of medals
            year_result = max(medals_by_year, key=medals_by_year.get)
            print(f'{country} has record of medals in {year_result}: {medals_by_year[year_result]} medals')
            medals_by_year.clear()
            #Reset while
            file.seek(0)
#4th task
def interactive(filename):
    country = input("Input country or its noc: ")
    #dictionary for 1st game
    temp_dict = {}
    #dictionary for best/worst games
    games_dict = {}
    all_medals_gold = 0
    all_medals_silver = 0
    all_medals_bronze = 0
    amt_games = 0
    
    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if not line: break

            # Split data by information
            info = line.split('\t')
            _team = info[6]
            _noc = info[7]
            _games = info[8]
            _year = info[9]
            _city = info[11]
            _medal = info[14]
            if country == _team or country == _noc:
                temp_dict[_city]=[int(_year)]
                if _games not in games_dict:
                    #initializing an item in dictionary in format [overall_medals, gold, silver, bronze]
                        games_dict[_games] = [0, 0, 0, 0]
                else:
                    if _medal != "NA":
                        if _medal == 'Gold\n': games_dict[_games][1] += 1
                        if _medal == 'Silver\n': games_dict[_games][2] += 1
                        if _medal == 'Bronze\n': games_dict[_games][3] += 1
                        #counting overall medals
                        games_dict[_games][0]=games_dict[_games][1]+games_dict[_games][2]+games_dict[_games][3]
                        
        #counting medals of each type and total amount of games
        for game in games_dict:
            all_medals_gold += games_dict[game][1]
            all_medals_silver += games_dict[game][2]
            all_medals_bronze += games_dict[game][3]
            amt_games += 1
        #avg for each medal
        avg_gold = all_medals_gold//amt_games
        avg_silver = all_medals_silver//amt_games
        avg_bronze = all_medals_bronze//amt_games
        #from my observation min(), max() for dictionary with lists as values
        #take min and max just from 1st item that's why we have overall amt of medals as index [0]
        worst_game = min(games_dict, key=games_dict.get)
        best_game = max(games_dict, key=games_dict.get)
        print(f"Best game: {best_game} with {games_dict[best_game][0]} medals. Worst game {worst_game} with {games_dict[worst_game][0]} medals.")
        print(f"Avg gold medals: {avg_gold}, Avg silver {avg_silver}, Avg bronze {avg_bronze}")

                
                
    
    first = min(temp_dict, key=temp_dict.get)
    print(f"First game: {first} ,{temp_dict[first]}")


    



def main():
    parser = argparse.ArgumentParser()
    # Add command
    parser.add_argument("--command","--c", required=False)
    parser.add_argument('--overall', nargs='+', required=False)
    # Add arguments
    parser.add_argument("--filename","--f", required=False)
    parser.add_argument("--country", required=False)
    parser.add_argument("--year","--y", required=False)
    parser.add_argument("--output", type=bool, required=False)

    args = parser.parse_args()

    if args.command == "medals":
        medals(args.filename, args.country, args.year, args.output)
    if args.command == "total":
        total(args.filename, args.year)
    if args.overall:
        overall(args.filename, args.overall)
    if args.command == "interactive":
        interactive(args.filename)


main()
