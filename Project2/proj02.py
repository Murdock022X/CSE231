##################################################################
#   Computer Project #2
#   
#   Print a banner
#   Algorithm
#       prompt for A or B
#       loop until B is selected
#           prompt selection code
#           prompt for rental period
#           prompt for odometer readings
#           select suite based on selection code           
#               make apporpriate calculations
#               print the values
#           ask if user wants to continue
#       
##################################################################


import math   #get math module

#displays the banner and prompts
print("\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)")

cont = input('''\nWould you like to continue (A/B)? ''')    #inputs a character

#if inputted char is B print, if not a or b display error message
if cont == 'B':
    print('Thank you for your loyalty.')

#display error if not A or B
while not(cont == 'A' or cont == 'B'):
    print('*** Invalid customer code. Try again. ***')
    cont = input('Would you like to continue (A/B)? ')

#create while loop active while cont is A will loop until user selects B
#It was difficult getting the while loop to exit correctly if B was entered
#It was also difficult getting the loop to reprompt for 'A' or 'B'
while cont == 'A':
    code_str = input('Customer code (BD, D, W): ')  #enters code
    
    while not(code_str == 'BD' or code_str == 'D' or code_str == 'W'):
        print("\n\t*** Invalid customer code. Try again. ***")
        code_str = input('Customer code (BD, D, W): ')
        
    #inputs days and odometer readings
    days = input('\nNumber of days: ')
    start = input('Odometer reading at the start: ')
    end = input('Odometer reading at the end:   ')
    
    #converts inputs to ints
    days = int(days)
    start = int(start)
    end = int(end)
    
    #selection code selects a suite of code
    if code_str == 'BD':
        
        #calculates miles based on whether the odometer rolled over
        if end < start: 
            miles = (1000000 - start) + end
            miles = miles/10
        else:
            miles = (end - start)
            miles = miles/10
        
        #calulates the total costs and mileage costs
        base_cost = 40.0*days
        mileage_cost = 0.25*miles
        cost = float(mileage_cost + base_cost)
        
        #prints a summary of the bill
        print('\nCustomer summary:')
        print('\tclassification code:', code_str)
        print('\trental period (days):', days)
        print('\todometer reading at start:', start)
        print('\todometer reading at end:  ', end)
        print('\tnumber of miles driven: ', miles)
        print('\tamount due: $', round(cost, 2))
        
    elif code_str == 'D':
        
        #calculates miles based on whether the odometer rolled over
        if end < start:
            miles = (1000000 - start) + end
            miles = miles/10
        else:
            miles = (end - start)
            miles = miles/10
            
        base_cost = 60*days
        
        #uses different mileage cost equations based on miles per day
        if (miles/days) <= 100:
            mileage_cost = 0
        else:
            over = miles - 100*days
            mileage_cost = 0.25*over
        cost = float(mileage_cost + base_cost)
        
        #prints a summary of the bill
        print('\nCustomer summary:')
        print('\tclassification code:', code_str)
        print('\trental period (days):', days)
        print('\todometer reading at start:', start)
        print('\todometer reading at end:  ', end)
        print('\tnumber of miles driven: ', miles)
        print('\tamount due: $', round(cost, 2))
        
    elif code_str == 'W':
        
        weeks = math.ceil(days/7)   #weeks var needed for cost calcs
        
        #calculates miles based on whether the odometer rolled over
        if end < start:
            miles = (1000000 - start) + end
            miles = miles/10
        else:
            miles = (end - start)
            miles = miles/10
            
        base_cost = 190*weeks
        
        #uses differnt mileage cost equations based on miles per week
        if (miles/weeks) <= 900:
            mileage_cost = 0
        elif 900 < (miles/weeks) <= 1500:
            mileage_cost = 100*weeks
        else:
            over = miles - 1500*weeks
            mileage_cost = 200*weeks + 0.25*over
        cost = float(mileage_cost + base_cost)
        
        #prints a summary of the bill
        print('\nCustomer summary:')
        print('\tclassification code:', code_str)
        print('\trental period (days):', days)
        print('\todometer reading at start:', start)
        print('\todometer reading at end:  ', end)
        print('\tnumber of miles driven: ', miles)
        print('\tamount due: $', round(cost, 2))
    
    #input a A or B to continue or stop
    cont = input('''\nWould you like to continue (A/B)? ''')
    print()
    
    if cont == 'B': #Exits if B
        print('Thank you for your loyalty.')
    
    while not(cont == 'A' or cont == 'B'):  #displays error msg and reprompts
        print('\n\t*** Invalid customer code. Try again. ***')
        cont = input('Would you like to continue (A/B)? ')