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

    res_list = []

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
