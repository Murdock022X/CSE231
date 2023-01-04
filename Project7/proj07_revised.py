import csv
from operator import itemgetter

REGIME=["Closed autocracy","Electoral autocracy","Electoral democracy",\
        "Liberal democracy"]
MENU='''\nRegime Options:
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes        
    '''

def open_file():
    '''Takes no input, prompts for file name. Attempts to open file.
    If file not found displays error then re-prompts.'''
    
    #run the loop so we dont ask for input inside the loop and outside
    file_not_found = False
    while file_not_found == False:
        
        #try to create a file pointer and if not found generate error message 
        #and prompt again
        try:
            input_file_str = input("Enter a file: ")
            fp = open(input_file_str)
            return fp
        except FileNotFoundError:
            print("File not found. Please try again.")
            file_not_found = False

def read_file(fp):
    '''Takes a file pointer. Reads the csv file. Creates a list of 
    country names (located at index 1 in each line). Then political regime
    data stored as list of ints. Once new country is found in data appends the
    list of political regime data to a list of lists. Returns country names
    list and list of lists of poltical regime data.'''

    master_dict = {}
    reader = csv.reader(fp)   #read the data with the csv reader
    next(reader)   #skip the header

    for line in reader:
        if line[1] not in master_dict:
            master_dict[line[1]] = [int(line[4])]
        else:
            list_of_values = master_dict[line[1]]
            list_of_values.append(line[4])
            master_dict[line[1]] = list_of_values

    return master_dict
        
def history_of_country(country, master_dict):
    '''Takes a country, list of country names, list of data on the governements
    of regimes and return the type of government that is most common throughout
    the country's history. Goes with the more authoritarian government in the 
    case of a tie.'''
    
    country_regime_data_list = master_dict[country]

    #finds the number of times each number 0-3 occurs
    type_zero_count_int = country_regime_data_list.count(0)
    type_one_count_int = country_regime_data_list.count(1)
    type_two_count_int = country_regime_data_list.count(2)
    type_three_count_int = country_regime_data_list.count(3)
    
    #creates a list of those counts
    list_of_counts = [type_zero_count_int,type_one_count_int,
                      type_two_count_int,type_three_count_int]

    #Will return the maximum and tie breaker already works because the lower 
    #regime value will be encountered first in the case of a tie.
    list_of_counts_max = max(list_of_counts)
    
    #indexes the list of counts for the max
    dominant_type_int = list_of_counts.index(list_of_counts_max)
    type_str = REGIME[dominant_type_int]
    
    return type_str
    
def historical_allies(regime, master_dict):
    '''Takes a regime, list of country names, and list of data on the regimes
    then finds the dominant type of regime using the history_of_country() 
    function of all countrys, then selects which ones share the regime type
    specified.'''

    #takes the type of regime and finds the integer value
    type_int = REGIME.index(regime)
    
    index = 0
    all_allies_list =[]
    
    for country, regime_data_list in master_dict.items():
        #uses history_of_country function to find the most common type of
        #government.
        gov_type_str = history_of_country(country, master_dict)
        
        #indexs the REGIME list looking for the type of government to return 
        #the associated number value.
        ally_type_int = REGIME.index(gov_type_str)
        
        #if the type found is equal to the value we search for we append the 
        #country name.
        if ally_type_int == type_int:
            all_allies_list.append(country)
            
        index += 1
    
    return all_allies_list

def top_coup_detat_count(top, master_dict):          
    '''Takes an int, list of country names, and list of lists of regime data.
    Then it finds the number of changes that occur for each country and makes
    a tuple with the country name, then the number of changes. Then it adds the
    tuples to a list and sorts by the number of changes. Then it gives only a
    specific number of countrys.'''

    list_of_changes = []

    #takes the data from each tuple and extracts it
    for country, regime_data_list in master_dict.items():
        prev_value = -1
        count_of_changes = 0
        
        #takes the list inside the tuple and extracts it
        for gov_type in regime_data_list:
            
            #if the government type changes then add 1 to the count of changes
            if gov_type != prev_value:
                count_of_changes += 1
            
            #updates the previous value for the next iteration
            prev_value = gov_type
        
        #must subtract one because loop starts with a number it will never be 
        #so an extra count is added and therefore must be subtracted.
        count_of_changes -= 1
        
        #changes them into tuples
        country_changes_tup = (country, count_of_changes)
        
        #appends the tuple to the master list of changes
        list_of_changes.append(country_changes_tup)

    list_of_changes.reverse()   #reverses to reverse alphabetical
    #sorts by number of changes
    list_of_changes = sorted(list_of_changes, key=itemgetter(1), reverse=True)
  #reverses again to go to highest at top of list
    
    list_of_changes = list_of_changes[:top]   #takes only the number asked for

    return list_of_changes
    
def main():
    
    fp = open_file()   #generate file pointer
    
    #read the file into the lists
    master_dict = read_file(fp)

    print(MENU)   #print the menu
    options = ['q','1','2','3']   #valid options list
    
    option_str = input("Input an option (Q to quit): ")   #input choice
    
    if option_str.isalpha():   #if string is alphabetic convert to lowercase
        option_str = option_str.lower()
        
    while not(option_str in options):   #if the string not in options try again
        print("Invalid choice. Please try again.")
        option_str = input("Input an option (Q to quit): ")
        if option_str.isalpha():   #if string is alphabetic convert to lower
            option_str = option_str.lower()
            
    while option_str != 'q':   #run while not q
        
        if option_str == '1':
            country_input_str = input("Enter a country: ")   #input country
            
            #makes sure the country is valid
            while not(country_input_str in master_dict):
                print("Invalid country. Please try again.")
                country_input_str = input("Enter a country: ")
            "\nHistorically {} has mostly been an {}"
            
            #calls the appropriate function
            dominant_type_str = history_of_country(country_input_str, \
                                                   master_dict)
                
            #formats and prints correctly an for vowels and a for non-vowels
            if (dominant_type_str == 'Electoral democracy') or \
            (dominant_type_str == 'Electoral autocracy'):
                print("\nHistorically {} has mostly been an {}".format \
                      (country_input_str, dominant_type_str))
            else:
                print("\nHistorically {} has mostly been a {}".format \
                      (country_input_str, dominant_type_str))
        
        elif option_str == '2':
            regime_input_str = input("Enter a regime: ")   #prompts for regime
            
            #ensures a valid regime is selected
            while not(regime_input_str in REGIME):
                print("Invalid regime. Please try again.")
                regime_input_str = input("Enter a regime: ")
            
            #calls the historical_allies function to generate a list of allies
            list_of_historical_allies = historical_allies(regime_input_str, \
                                master_dict)
            
            allies_str = ''
            
            #formats a string that ends with ', ' after each country
            for ally in list_of_historical_allies:
                allies_str = allies_str + ', ' + ally
            
            allies_str = allies_str.strip(' ,')   #strips the ', ' at end
            
            print("\nHistorically these countries are allies of type:", \
                  regime_input_str)
            
            print(allies_str)
            
        elif option_str == '3':
            #ask for input on how many countries to show
            input_top_str = input("Enter how many to display: ")
            
            positive_bool = False
            digit_bool = False  
            
            #makes sure that the number is positive and an integer
            while (positive_bool == False) or (digit_bool == False):
                try:
                    input_top_int = int(input_top_str)    
                    if input_top_int > 0:
                        digit_bool = True
                        postive_bool = True
                        break
                    else:
                        print("Invalid number. Please try again.")
                        input_top_str = input("Enter how many to display: ")
                        
                except ValueError:
                    print("Invalid number. Please try again.")
                    input_top_str = input("Enter how many to display: ")
            
            #calls top_coup_detat_count function to find the list of tuples
            country_changes_list = top_coup_detat_count(input_top_int, 
                                master_dict)
            
            print("{: >25} {: >8}".format("Country", "Changes")) #header
            count = 1
            for country in country_changes_list:
                if count == 1:
                    #only print this if first in print sequence
                    print("\n{: >25} {: >8}".format(country[0], country[1]))
                else:
                    print("{: >25} {: >8}".format(country[0], country[1]))
                count += 1
        
        print(MENU)   #print menu again
        option_str = input("Input an option (Q to quit): ")   #take input
        
        if option_str.isalpha():   #convert to lower if applicable
            option_str = option_str.lower()
        
        while not(option_str in options):   #ensure valid input
            print("Invalid choice. Please try again.")
            option_str = input("Input an option (Q to quit): ")
            if option_str.isalpha():
                option_str = option_str.lower()
        
    print("The end.")

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main() 