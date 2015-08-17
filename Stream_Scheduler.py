import datetime

scheduling = True
VODS_Scheduled = {}
live_Scheduled = {}
episodic_Scheduled = {}
playlist_Scheduled = {}
Scheduled = {}

def run_of_show():
    '''
    '''
    date_entry = input('Enter show start date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    start_date = datetime.date(year,month,day)

    time_entry = input('Enter show start time in hh:mm:ss format: ')
    hour, minute, second = map(int, time_entry.split(':'))
    start_time = datetime.time(hour,minute,second)

    show_length_entry = input('Enter length of show in days: ')
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
        VOD_name = input('Enter the name of your VOD: ')
        VOD_name = str(VOD_name)
        VOD_Details.append(VOD_name)
        VOD_duration_entry = input('Enter the length in hh:mm:ss format: ')
        VOD_hour, VOD_minute, VOD_second = map(int, VOD_duration_entry.split(':'))
        VOD_duration = datetime.timedelta(hours=VOD_hour, minutes=VOD_minute, seconds=VOD_second)
        VOD_duration = int(VOD_duration.total_seconds())
        VOD_Details.append(VOD_duration)
        VOD_date_entry = input('Enter show start date in YYYY-MM-DD format: ')
        VOD_year, VOD_month, VOD_day = map(int, VOD_date_entry.split('-'))
        media_start_date = datetime.date(VOD_year,VOD_month,VOD_day)
        VOD_Details.append(media_start_date)
        #VODS_Scheduled[VOD_start_date] = VOD_Details
        Scheduled[media_start_date] = VOD_Details
        #continue
        pass

    elif media_type == "live":
        live_Details = []
        live_Name = input('Enter the name of your live stream: ')
        live_Name = str(live_Name)
        live_Details.append(live_Name)
        live_Duration_entry = input('Enter the length of your live-stream in hh:mm:ss format. Enter -1 to go until complete: ')
        if live_Duration_entry == '-1':
            live_Duration = int(live_Duration_entry)
        else:
            live_Hour, live_Minute, live_Second = map(int, live_Duration_entry.split(':'))
            live_Duration = datetime.timedelta(hours=live_Hour, minutes=live_Minute, seconds=live_Second)
            live_Duration = int(live_Duration.total_seconds())
        live_Details.append(live_Duration)
        Live_date_entry = input('Enter show start date in YYYY-MM-DD format: ')
        Live_year, Live_month, Live_day = map(int, Live_date_entry.split('-'))
        media_start_date = datetime.date(Live_year,Live_month,Live_day)
        live_Details.append(media_start_date)
        Live_starttime_entry = input('Enter show start time in hh:mm:ss format: ')
        Live_starttime_hour, Live_starttime_minute, Live_starttime_second = map(int, Live_starttime_entry.split(':'))
        Live_start_time = datetime.time(Live_starttime_hour, Live_starttime_minute, Live_starttime_second)
        live_Details.append(Live_start_time)
        #live_Scheduled[Live_start_date] = live_Details
        media_start_entry = datetime.datetime(Live_year, int(Live_month), int(Live_day), Live_starttime_hour, Live_starttime_minute, Live_starttime_second)
        format = "%Y-%m-%d %H:%M:%S"
        media_start = datetime.datetime.strftime(media_start_entry, format)
        live_Details.append(media_start)
        Scheduled[media_start] = live_Details
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
        cont = input('Would you like to continue? Y/N')
        if cont == 'Y':
            media_type = input('What type of media would you like to schedule? (VOD, live, episodic, playlist. Type stop to print')
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
#print (VODS_Scheduled)
#print (live_Scheduled)
print (Scheduled)
#print('All Finished!')