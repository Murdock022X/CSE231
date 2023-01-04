#############################################################################
#   
#   Computer Project #05
#
#   Wave Data & Surf Analyzer
#   
#   Create open_file() function to create the file string and evaluate if it 
#   is valid
#   
#   Create get_month_str(mm) function to change a month
#   in digits to three letter abbrev. 
#   
#   Create best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,
#   best_dpd) function to evaluate when best surf conditions are by comparing 
#   previous best surf to surf in new line. If a tie, if the dpd is greater 
#   then the new values become the new best.
#
#   Create main() to activate main sequence. Intializes appropriate values 
#   then iterates through each line in the file taking the values evaluating 
#   for mins, maxs, storing the new wvht in a sum and taking a count to be 
#   used for average wvht. Then calls best surf function to evaluate as 
#   previously described. Then prints all values in appropriate format.
#
#############################################################################

#tries to open a file and if not found returns false
def valid_file(txt_file):
    try:
        test_file = open(txt_file, "r")
        return True
    except FileNotFoundError:
        return False

#asks for input year then creates the appropriate file str calls the 
#valid_file function to ensure valid input, loops until valid. 
#Then opens the file for reading
def open_file():
    year_of_data_str = input("Input a year: ")
    
    #formats the file string
    txt_file_str = 'wave_data_' + year_of_data_str + '.txt'
    
    #if the file is not found it repeats
    while not(valid_file(txt_file_str)):
        print("File does not exist. Please try again.")
        year_of_data_str = input("Input a year: ")
        txt_file_str = 'wave_data_' + year_of_data_str + '.txt'
    
    wave_data_file = open(txt_file_str) #Opens file
    return wave_data_file 

#takes the number of a month and returns the three letter abbrev.
def get_month_str(mm):
    if mm == '01':
        return 'Jan'
    elif mm == '02':
        return 'Feb'
    elif mm == '03':
        return 'Mar'
    elif mm == '04':
        return 'Apr'
    elif mm == '05':
        return 'May'
    elif mm == '06':
        return 'Jun'
    elif mm == '07':
        return 'Jul'
    elif mm == '08':
        return 'Aug'
    elif mm == '09':
        return 'Sep'
    elif mm == '10':
        return 'Oct'
    elif mm == '11':
        return 'Nov'
    elif mm == '12':
        return 'Dec'

#takes the current values for month, day, hr, wvht, and dpd. Along with 
#previous bests. Then evaluates whether they are better.
def best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd):
    
    #if the wvht is higher and the hour is after 6am or before 7pm make all
    #associated values equal to bests
    if (wvht > best_wvht) and (19 > hr > 6):
        best_mm = mm
        best_dd = dd
        best_hr = hr
        best_wvht = wvht
        best_dpd = dpd
    
    #if there is a tie in wvht then check if the dpd is higher and again check
    #if hour is after 6am and before 7pm 
    elif (wvht == best_wvht) and (dpd > best_dpd) and (19 > hr > 6):
        best_mm = mm
        best_dd = dd
        best_hr = hr
        best_wvht = wvht
        best_dpd = dpd
    
    
    return best_mm, best_dd, best_hr, best_wvht, best_dpd

def main():  
    
    print("Wave Data")
    
    #intializes values
    mm_str = '04'
    dd_str = '02'
    hr_int = 0
    wvht_float = 0.0
    dpd_float = 0.0
    
    min_wvht_float = 10**6
    max_wvht_float = 0.0

    wvht_total_float = 0.0
    
    best_mm = '04'
    best_dd = '02'
    best_hr = 0
    best_wvht = 0.0
    best_dpd = 0.0
    
    count = 0
    
    #call the open_file() function to get file then read the first two lines
    #to knock off the headers
    wave_data_file = open_file()
    wave_data_file.readline()
    wave_data_file.readline()
    
    for line_str in wave_data_file:
        mm_str = (line_str[5:7]).strip()    #finds the month in the line
        dd_str = (line_str[8:10]).strip()   #finds the day in the line
        hr_str = (line_str[11:13]).strip()  #finds the hour in the line
        wvht_str = (line_str[30:36]).strip()    #finds the wvht in the line
        dpd_str = (line_str[37:42]).strip()     #finds the dpd in the line
        
        #checks if the values are spurious and if they are not go into if
        #note: did not use continue because if spurious values then continue
        #did not continue
        if not(wvht_str == '99.00') and not(dpd_str == '99.00'):
            hr_int = int(hr_str)
            wvht_float = float(wvht_str)
            dpd_float = float(dpd_str)
            
            #sets min wvht if smaller
            if min_wvht_float > wvht_float:
                min_wvht_float = wvht_float
            
            #set max wvht if larger
            if max_wvht_float < wvht_float:
                max_wvht_float = wvht_float
                
            #creates a sum of wvht total
            wvht_total_float = wvht_total_float + wvht_float
            count += 1  #increase count by 1
            
            #calls best_surf function
            best_mm, best_dd, best_hr, best_wvht, best_dpd = \
            best_surf(mm_str, dd_str, hr_int, wvht_float, dpd_float,\
                 best_mm, best_dd, best_hr, best_wvht, best_dpd)
    
    average_wvht_float = wvht_total_float/count   #calculates averages
    print("\nWave Height in meters.")
    
    #prints average values
    print("{:7s}: {:4.2f} m".format('average', average_wvht_float)) 
    
    #prints maximum values
    print("{:7s}: {:4.2f} m".format('max', max_wvht_float))
    
    #prints minumum values
    print("{:7s}: {:4.2f} m".format('min', min_wvht_float))
    
    print("\nBest Surfing Time:")
    
    #prints columns for mth day hr wvht dpd
    print("{:3s} {:3s} {:2s} {:>6s} {:>6s}"\
          .format("MTH","DAY","HR","WVHT","DPD"))
    
    #prints bests for each value
    print("{:3s} {:>3s} {:2d} {:5.2f}m {:5.2f}s"\
          .format(get_month_str(best_mm), best_dd, \
                  best_hr, best_wvht, best_dpd))
        
        

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()