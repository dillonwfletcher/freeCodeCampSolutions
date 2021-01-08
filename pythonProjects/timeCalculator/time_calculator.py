# no external libraries allowed

def add_time(start, duration, dow=None):

    days_passed = 0

    s_arr = start.split()
    curr = s_arr[0].split(":")
    ap = s_arr[1] # this is AM or PM
    curr_hr, curr_min = int(curr[0]), int(curr[1])
    
    d_arr = duration.split(":")
    durr_hrs, durr_min = int(d_arr[0]), int(d_arr[1])
    
    # calc how many days will pass 
    days_passed = durr_hrs // 24    

    # set durration hours to just hours left over after full days passed
    durr_hrs %= 24

    # convert time to 24 hr time
    if ap == "PM":
        curr_hr += 12

        if curr_hr > 24: 
            curr_hr %= 24
    
    # calc new time
    new_hr = curr_hr + durr_hrs
    new_min = curr_min + durr_min
    
    # if more than 60 minutes add 1hr; set min
    if new_min >= 60:
        new_hr += 1
        new_min = new_min % 60
    
    #convert 24 hr time back to standard time
    # if hr 24 or higher time is in AM; calc new hour and add to days passed since we crossed over to new day
    if new_hr >= 24:
        ap = "AM"
        new_hr %= 24
        days_passed += 1

   
    # if 24 hr time in afternoon set period to PM calc afternoon hour
    if new_hr >= 12:
        ap = "PM"
        new_hr %= 12

    # if hr gets set to 0 24hr time set to 12 for standard time
    if new_hr == 0:
        new_hr = 12
    
    # turn time back into a string
    new_time = str(new_hr) + ":" + "{:02d} ".format(new_min) + ap
   
    # if day of the week was given
    # calc what day it is after duration has passed
    if dow:
        # weekday tuple
        dows = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

        # get index of weekday passed 
        idx = dows.index(dow.lower().title())

        # get new index after accounting for days passed
        idx += days_passed

        if idx > 7:
            idx %= 7

        # add weekday to return string
        new_time += ", {}".format(dows[idx])
 
    # add to return string to let user know how many days have passed
    if days_passed > 1:
        new_time += " ({} days later)".format(days_passed)
    elif days_passed == 1 :
        new_time += " (next day)" 

    return new_time
