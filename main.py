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
                            print(i)
                            #Print result
                            if i == 10:
                                print(res)
                                print(total_medals)
                                break
            if output == True:
                with open('result.txt','w') as file:
                    file.write(res)
                    file.write(total_medals)


def main():
    parser = argparse.ArgumentParser()
    #Add command
    parser.add_argument("--command", required=True)
    #Add arguments
    parser.add_argument("--filename", required=True)
    parser.add_argument("--country", required=True)
    parser.add_argument("--year", required=True)
    parser.add_argument("--output",type=bool, required=False)

    args = parser.parse_args()

    if args.command == "medals":
        medals(args.filename,args.country,args.year,args.output)


main()
