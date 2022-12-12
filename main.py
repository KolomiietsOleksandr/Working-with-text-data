import argparse

#First task
def medals(filename,country,year, output):
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

                #Split data by information
                info = line.split('\t')
                _name = info[1]
                _team = info[6]
                _noc = info[7]
                _year = info[9]
                _sport = info[12]
                _medal = info[14]
                if year == _year:
                    if country == _noc or country == _team:
                        if _medal != 'NA\n':
                            list = (f'{_name}-{_sport}-{_medal}')
                            #Count total medals
                            if _medal == 'Gold\n': gold += 1
                            if _medal == 'Silver\n': silver += 1
                            if _medal == 'Bronze\n': bronze += 1

                            total_medals = (f'Total medals: Gold - {gold}, Silver - {silver}, Bronze - {bronze}')
                            #Add result to list
                            res = res + res_list.join(list)
                            i += 1
                            
                            #Print result
                            if i == 10:
                                print(res)
                                print(total_medals)
                                break
            if output == True:
                with open('result.txt','w') as file:
                    file.write(res)
                    file.write(total_medals)

def total(filename,year):

    
    with open(filename, "r") as file:
            while True:
                line = file.readline()
                if not line: break

                #Split data by information
                info = line.split('\t')
                _team = info[6]
                _noc = info[7]
                _year = info[9]
                _medal = info[14]
                if year == _year:
                    #check if country already exists in dict
                    if _team not in C_M:
                        C_M[_team]= [0, 0, 0]
                    if _medal != 'NA\n':
                                #Count total medals
                                if _medal == 'Gold\n': C_M[_team][0] += 1
                                if _medal == 'Silver\n': C_M[_team][1] += 1
                                if _medal == 'Bronze\n': C_M[_team][2] += 1
    for country in C_M:
        total=C_M[country][0] + C_M[country][1] + C_M[country][2]
        if total < 1:
            continue
        else:
            print(f"{country} has total {total} medals: {C_M[country][0]} Gold, {C_M[country][1]} Silver, {C_M[country][2]}")
#Creating a dictionary that stores medals for each country                    
C_M = {

    }
                



def main():
    parser = argparse.ArgumentParser()
    #Add command
    parser.add_argument("--command", required=True)
    #Add arguments
    parser.add_argument("--filename", required=True)
    parser.add_argument("--country", required=False)
    parser.add_argument("--year", required=False)
    parser.add_argument("--output",type=bool, required=False)

    args = parser.parse_args()

    if args.command == "medals":
        medals(args.filename,args.country,args.year,args.output)
    if args.command == "total":
        total(args.filename,args.year)

main()
