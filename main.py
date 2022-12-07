user = input('Write information:')

try:
    input_info = user.split(' ')
    #Specify the data
    file_directory = input_info[0] #File name: Olympic_Data.tsv
    input_command = input_info[1]
    input_country = input_info[2]
    input_year = input_info[3]
except: print('Invalid data')

with open(file_directory, 'r') as file:
    file.readline() #Skip headlines

    #VARIABLES
    res_list = ''
    x = ''
    gold = 0
    silver = 0
    bronze = 0
    i = 0

    while True:
        line = file.readline()
        if not line: break

        #Split data by information
        info = line.split('	')
        name = info[1]
        team = info[6]
        noc = info[7]
        year = info[9]
        sport = info[12]
        medal = info[14]

        #Command -medals
        if input_command == '-medals':
            medals = True
            while medals == True:
                if medal != 'NA\n' and input_year == year:
                    if input_country == noc or input_country == team:

                        list = (f'{name}-{sport}-{medal}')

                        if medal == 'Gold\n': gold += 1
                        if medal == 'Silver\n': silver += 1
                        if medal == 'Bronze\n': bronze += 1

                        x = x + res_list.join(list)
                        i += 1

                        if i == 10:
                            print(x)
                            print(f'Total medals: Gold - {gold}, Silver - {silver}, Bronze - {bronze}')
                            medals = False
