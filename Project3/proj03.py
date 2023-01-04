###############################################################
#   Computer Project #3
#
#   Create a tuition calculator that asks for input
#   Input includes: class level and credits
#   If a senior or junior ask what college
#   If a freshman or sophomore ask if in college of engineering
#   If college is none ask if in James Madison
#   Ask for credit amount
#   Calculate total fees
#   Format into dollar amount
#
###############################################################


print('2021 MSU Undergraduate Tuition Calculator.\n')


#Stored Important values in easy variables
FRESH_PERCRED = 482
SOPH_PERCRED = 494
JRSR_PERCRED = 555

COE_BROAD_JRSR_PERCRED = 573

FRESH_FLAT = 7230
SOPH_FLAT = 7410
JRSR_FLAT = 8325

COE_BROAD_JRSR_FLAT = 8595

#Created a variable that decides whether the loop runs
cont = 'yes'
#Loops so that you can make another calculation
while cont == 'yes':
    
    #Asks for class level and converts to lower case
    level_str = input('Enter Level as freshman, sophomore, junior, senior: ')
    level_str = level_str.lower()
    
    #Checks if the input is valid and loops until valid input
    while not((level_str == 'freshman') or (level_str == 'sophomore') or \
    (level_str == 'junior') or (level_str == 'senior')):
        print('Invalid input. Try again.')
        level_str = input('Enter Level as freshman, \
sophomore, junior, senior: ')
        level_str = level_str.lower()
          
    #checks if sr/jr and asks for college input if either true
    if (level_str == 'junior') or (level_str == 'senior'):
        college_str = input('Enter college as business, engineering, \
health, sciences, or none: ')
        college_str = college_str.lower()
    
    #checks if a sophomore or freshman 
    #and asks for college of engineering input
    if (level_str == 'freshman') or (level_str == 'sophomore'):
        college_str = input('Are you admitted to the College of Engineering \
(yes/no): ')
        college_str = college_str.lower()

    #If you are not in a college and you are a senior or \
    #junior, check if in J Madison College
    if ((level_str == 'junior') or (level_str == 'senior')) and \
    not((college_str == 'engineering') or (college_str == 'business') \
    or (college_str == 'health') or (college_str == 'sciences')):
        jmadison_str = input('Are you in the James Madison \
College (yes/no): ')
        jmadison_str = jmadison_str.lower()
        if not(jmadison_str == 'yes'):
            jmadison_str == 'no'
    
    if ((level_str == 'freshman') or (level_str == 'sophomore')) and \
    not(college_str == 'yes'):
        jmadison_str = input('Are you in the James Madison \
College (yes/no): ')
        jmadison_str = jmadison_str.lower()
        if not(jmadison_str == 'yes'):
            jmadison_str == 'no'
            
    #Input Credits and check if a digit that is less than one 
    #if neither true ask again
    credits_str = input('Credits: ')
    while not(credits_str.isdigit()):
        print('Invalid input. Try again.')
        credits_str = input('Credits: ')
    
    credits_int = int(credits_str)
    
    while credits_int < 1:
        print('Invalid input. Try again.')
        credits_str = input('Credits: ')
        while not(credits_str.isdigit()):
            print('Invalid input. Try again.')
            credits_str = input('Credits: ')
        credits_int = int(credits_str)
    
    #Calculate fees if a freshman
    if level_str == 'freshman':
        
        #Calculate if in college of engineering
        if college_str == 'yes':
            
            #Calculate if over 18 credits
            if credits_int > 18:
                credits_over_int = credits_int - 18
                fees = FRESH_FLAT + \
                (FRESH_PERCRED*credits_over_int) + 670
            
            #Calculate if greater than or equal to 12 credits 
            #and less than or equal to 18 credits
            elif 12 <= credits_int <= 18:
                fees = FRESH_FLAT + 670

            #Calculate if less than 12 credits
            elif 1 <= credits_int <= 11:
                if credits_int > 4:
                    fees = FRESH_PERCRED*credits_int + 670
                elif credits_int <= 4:
                    fees = FRESH_PERCRED*credits_int + 402
                
        #Calculate if not in college of engineering
        elif college_str == 'no':

            #Calculate if over 18 credits
            if credits_int > 18:
                credits_over_int = credits_int - 18
                fees = FRESH_FLAT + \
                (FRESH_PERCRED*credits_over_int)

            #Calculate if greater than or equal to 12 credits 
            #and less than or equal to 18 credits
            elif 12 <= credits_int <= 18:
                fees = FRESH_FLAT
                    
            elif 1 <= credits_int <= 11:
                    fees = FRESH_PERCRED*credits_int
    
    #Calculate if a sophomore                    
    if level_str == 'sophomore':

        #Calculate if in college of engineering
        if college_str == 'yes':

            #Calculate if over 18 credits
            if credits_int > 18:
                credits_over_int = credits_int - 18
                fees = SOPH_FLAT + \
                (SOPH_PERCRED*credits_over_int) + 670

            #Calculate if greater than or equal to 12 credits 
            #and less than or equal to 18 credits
            elif 12 <= credits_int <= 18:
                fees = SOPH_FLAT + 670

            #Calculate if less than 12 credits
            elif 1 <= credits_int <= 11:
                if credits_int > 4:
                    fees = SOPH_PERCRED*credits_int + 670
                elif credits_int <= 4:
                    fees = SOPH_PERCRED*credits_int + 402

        #Calculate if not in college of engineering
        elif college_str == 'no':

            #Calculate if over 18 credits            
            if credits_int > 18:
                credits_over_int = credits_int - 18
                fees = SOPH_FLAT + \
                (SOPH_PERCRED*credits_over_int)

            #Calculate if greater than or equal to 12 credits 
            #and less than or equal to 18 credits
            elif 12 <= credits_int <= 18:
                fees = SOPH_FLAT

            #Calculate if less than 12 credits
            elif 1 <= credits_int <= 11:
                    fees = SOPH_PERCRED*credits_int

    #Calculate if a junior or senior                    
    if (level_str == 'junior') or (level_str == 'senior'):
        
        #use this loop if in business college
        if college_str == 'business':

            #Calculate if over 18 credits            
            if credits_int > 18:
                credits_over_int = credits_int - 18
                fees = COE_BROAD_JRSR_FLAT + \
                (COE_BROAD_JRSR_PERCRED*credits_over_int) + 226

            #Calculate if greater than or equal to 12 credits 
            #and less than or equal to 18 credits
            elif 12 <= credits_int <= 18:
                fees = COE_BROAD_JRSR_FLAT + 226

            #Calculate if less than 12 credits                
            elif 1 <= credits_int <= 11:
                if credits_int > 4:
                    fees = COE_BROAD_JRSR_PERCRED*credits_int + 226
                elif credits_int <= 4:
                    fees = COE_BROAD_JRSR_PERCRED*credits_int + 113
        
        #Calculate if in engineering college
        elif college_str == 'engineering':   

            #Calculate if over 18 credits            
            if credits_int > 18:
                credits_over_int = credits_int - 18
                fees = COE_BROAD_JRSR_FLAT + \
                (COE_BROAD_JRSR_PERCRED*credits_over_int) + 670

            #Calculate if greater than or equal to 12 credits 
            #and less than or equal to 18 credits
            elif 12 <= credits_int <= 18:
                fees = COE_BROAD_JRSR_FLAT + 670

            #Calculate if less than 12 credits                    
            elif 1 <= credits_int <= 11:
                if credits_int > 4:
                    fees = COE_BROAD_JRSR_PERCRED*credits_int + 670
                elif credits_int <= 4:
                    fees = COE_BROAD_JRSR_PERCRED*credits_int + 402
        
        #Calculate if in health or sciencees college
        elif (college_str == 'health') or (college_str == 'sciences'):

            #Calculate if over 18 credits            
            if credits_int > 18:
                credits_over_int = credits_int - 18
                fees = JRSR_FLAT + \
                (JRSR_PERCRED) + 100

            #Calculate if greater than or equal to 12 credits 
            #and less than or equal to 18 credits
            elif 12 <= credits_int <= 18:
                fees = JRSR_FLAT + 100

            #Calculate if less than 12 credits                
            elif 1 <= credits_int <= 11:
                if credits_int > 4:
                    fees = JRSR_PERCRED*credits_int + 100
                elif credits_int <= 4:
                    fees = JRSR_PERCRED*credits_int + 50
        
        #Use this loop if in James Madison
        elif jmadison_str == 'yes':

            #Calculate if over 18 credits
            if credits_int > 18:
                credits_over_int = credits_int - 18
                fees = JRSR_FLAT + \
                (JRSR_PERCRED*credits_over_int) + 7.5

            #Calculate if greater than or equal to 12 credits 
            #and less than or equal to 18 credits
            elif 12 <= credits_int <= 18:
                fees = JRSR_FLAT + 7.5

            #Calculate if less than 12 credits          
            elif 1 <= credits_int <= 11:
                fees = JRSR_PERCRED*credits_int + 7.5
        
        #Calculate if not in a specific college
        elif jmadison_str == 'no':
            if credits_int > 18:
                credits_over_int = credits_int - 18
                fees = JRSR_FLAT + \
                (JRSR_PERCRED*credits_over_int)

            #Calculate if greater than or equal to 12 credits 
            #and less than or equal to 18 credits
            elif 12 <= credits_int <= 18:
                fees = JRSR_FLAT

            #Calculate if less than 12 credits
            elif 1 <= credits_int <= 11:
                fees = JRSR_PERCRED*credits_int
    
    #All around undergrad fees
    fees = fees + 24
    
    #State News Tax
    if 6 <= credits_int:
        fees += 5
    
    #Formats into dollar amount
    tuition = 'Tuition is ${:,.2f}.'.format(fees)
    print(tuition)
    
    #Do it again?
    cont = input('Do you want to do another calculation (yes/no): ')
    cont = cont.lower()
        