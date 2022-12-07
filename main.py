user = input('Write information:')

try:
    input_info = user.split(' ')
    #Specify the data
    file_directory = input_info[0] #File name: Olympic_Athletes-athlete_events.tsv
    input_command = input_info[1]
    input_country = input_info[2]
    input_year = input_info[3]
except: print('Invalid data')
