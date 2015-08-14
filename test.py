import datetime
scheduling = True

def run_of_show():
    date_entry = input('Enter show start date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    start_date = datetime.date(year,month,day)

    time_entry = input('Enter show start time in hh:mm:ss format: ')
    hour, minute, second = map(int, time_entry.split(':'))
    start_time = datetime.time(hour,minute,second)

    show_length_entry = input('Enter length of show in days: ')
    show_length = int(show_length_entry)

    end_date = start_date + datetime.timedelta(days=show_length)

determine_run_of_show = input('Would you like to determine the run of show? Y/N: ')
determine_run_of_show = str(determine_run_of_show)
if determine_run_of_show == 'Y':
    run_of_show()

while scheduling:
    media_type = input('What type of media would you like to schedule? (VOD, live, episodic, playlist. Type stop to print): ')
    media_type = str(media_type)

    if media_type == "VOD":
        VOD_name = input('Enter the name of your VOD: ')
        VOD_name = str(VOD_name)
        VOD_duration_entry = input('Enter the length in hh:mm:ss format: ')
        VOD_hour, VOD_minute, VOD_second = map(int, VOD_duration_entry.split(':'))
        VOD_duration = datetime.timedelta(hours=VOD_hour, minutes=VOD_minute, seconds=VOD_second)
        VOD_duration = int(VOD_duration.total_seconds())
        VOD_date_entry = input('Enter show start date in YYYY-MM-DD format: ')
        VOD_year, VOD_month, VOD_day = map(int, VOD_date_entry.split('-'))
        VOD_start_date = datetime.date(VOD_year,VOD_month,VOD_day)
        continue

    elif media_type == "live":
        continue

    elif media_type == "episodic":
        continue

    elif media_type == "playlist":
        continue

    elif media_type == "stop":
        print ("VOD info- name:", VOD_name, "duration:", VOD_duration, "start date:", VOD_start_date)

        scheduling = False

print ("Show start: ", start_date, start_time)
print ("Show end: ", end_date)
