import datetime

scheduling = True
VODS_Scheduled = {}
live_Scheduled = {}
episodic_Scheduled = {}
playlist_Scheduled = {}

def run_of_show():
    '''
    '''
    date_entry = raw_input('Enter show start date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    start_date = datetime.date(year,month,day)

    time_entry = raw_input('Enter show start time in hh:mm:ss format: ')
    hour, minute, second = map(int, time_entry.split(':'))
    start_time = datetime.time(hour,minute,second)

    show_length_entry = raw_input('Enter length of show in days: ')
    show_length = int(show_length_entry)

    end_date = start_date + datetime.timedelta(days=show_length)
    return start_date, start_time, end_date

def set_scheduling(media_type):
    '''
    '''
    #media_type = 'VOD'
    scheduling = True
    if media_type == "VOD":
        VOD_Details = []
        VOD_name = raw_input('Enter the name of your VOD: ')
        VOD_name = str(VOD_name)
        VOD_Details.append(VOD_name)
        VOD_duration_entry = raw_input('Enter the length in hh:mm:ss format: ')
        VOD_hour, VOD_minute, VOD_second = map(int, VOD_duration_entry.split(':'))
        VOD_duration = datetime.timedelta(hours=VOD_hour, minutes=VOD_minute, seconds=VOD_second)
        VOD_duration = int(VOD_duration.total_seconds())
        VOD_Details.append(VOD_duration)
        VOD_date_entry = raw_input('Enter show start date in YYYY-MM-DD format: ')
        VOD_year, VOD_month, VOD_day = map(int, VOD_date_entry.split('-'))
        VOD_start_date = datetime.date(VOD_year,VOD_month,VOD_day)
        VOD_Details.append(VOD_start_date)
        VODS_Scheduled[VOD_name] = VOD_Details
        #continue

    elif media_type == "live":
        #continue
        pass

    elif media_type == "episodic":
        #continue
        pass
    
    elif media_type == "playlist":
        #continue
        pass
        
    elif media_type == "stop":
        #print ("VOD info- name:", VOD_name, "duration:", VOD_duration, "start date:", VOD_start_date)
        scheduling = False
        #break
        pass
            
def loop_scheduling():
    cont = 'Y'
    while cont == 'Y':
        cont = raw_input('Would you like to continue? Y/N')
        if cont == 'Y':
            media_type = raw_input('What type of media would you like to schedule? (VOD, live, episodic, playlist. Type stop to print')
            set_scheduling(media_type)
        elif cont == 'N':
            print('All Finished!')
            break
        else:
            print('Please input Y or N only.')
            continue
    

times = run_of_show()
#media_type = raw_input('What type of media would you like to schedule? (VOD, live, episodic, playlist. Type stop to print')
#set_scheduling(media_type)
loop_scheduling()

start_date = times[0]
start_time = times[1]
end_date = times[2]

print ("Show start: ", start_date, start_time)
print ("Show end: ", end_date)
#print('All Finished!')