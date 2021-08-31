def separate_time(time):
    start_h = int(time.split(" ")[0].split(":")[0])
    start_m = int(time.split(" ")[0].split(":")[1])
    try:
        meridian = time.split(" ")[1]
        if meridian == "PM": start_h += 12
    except:
        pass
    return start_h, start_m

def get_days(day_pass, day):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    result =""
    if day:
        result += ", "
        idx = week.index(day.title())
        for i in range(1,day_pass+1):
            day = week[idx+i]
            print(day,idx, i,idx+i)
            if idx+i==6: idx -= 7
        result +=day

    if day_pass or day:
        if day_pass ==1: result += f" (next day)"
        elif day_pass==0: pass 
        else: result += f" ({day_pass} days later)"
    else:
        result=""

    return result

def add_time(start, duration, day=False):
    #print(start, duration, day)
    start_h, start_m = separate_time(start)
    duration_h, duration_m =  separate_time(duration)
    final_m = start_m + duration_m
    final_h = start_h + duration_h + final_m//60
    final_m = str(final_m%60).zfill(2)
    day_pass = final_h//24
    

    if day_pass: final_h-= (day_pass*24)

    if final_h//12   :
         meridian="PM" 
         if final_h>12 :final_h -=12
    else:
         meridian="AM"
         if final_h==0: final_h+=12
    
    
    day_pass = get_days(day_pass, day)
    result = f"{final_h}:{final_m} {meridian}{day_pass}"


    print(result)
    print("____________________")

    return result




#changes format to 24 hours if is pm add 12 hours

