###############################################################################
#
#   Computer Project #6
#   
#   Program that reads data from a csv file into a master list and can sort
#   the list in various ways. 
#
#   get_option gets an option from the user to select which decides how to 
#   sort the list.
#
#   open_file asks the user which file they want to access, generates a file 
#   pointer, and ensures the file is valid.
#
#   read_file reads the data from the csv file into a master list converting
#   all elements in the list of lists to be appropriately typed for operations.
#
#   get_christmas_songs seperates the titles of each song into their component 
#   words and then checks if any of those words are in the christmas 
#   words list. If they are it adds the song to a list of christmas songs
#   and then returns the list.
#
#   sort_by_peak uses the peak rank to sort the songs.
#
#   sort_by_weeks_on_list uses the number of weeks the song has been on the 
#   list to sort.
#
#   song_score takes any given song and assigns a score based on the equation
#   score = A*peak_rank + B*rank_delta + C*weeks_on_list + D*curr_rank, where 
#   A,B,C,D are defined constants. rank_delta is the rank minus the previous 
#   weeks rank. curr_rank is 100-rank unless rank = -1 in which case 
#   curr_rank = -1.
#
#   sort_by_score just sorts the songs by score.
#
#   main runs the main and implements the functions.
#
###############################################################################

import csv
from operator import itemgetter
import copy

# Keywords used to find christmas songs in get_christmas_songs()
CHRISTMAS_WORDS = ['christmas', 'navidad', 'jingle', 'sleigh', 'snow',\
                   'wonderful time', 'santa', 'reindeer']

# Titles of the columns of the csv file. used in print_data()
TITLES = ['Song', 'Artist', 'Rank', 'Last Week', 'Peak Rank', 'Weeks On']

# ranking parameters -- listed here for easy manipulation
A,B,C,D = 1.5, -5, 5, 3

#The options that should be displayed
OPTIONS = "\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program \n"

#the prompt to ask the user for an option
PROMPT = "Enter one of the listed options: "

#prompts for user to select an option
def get_option():
    print(OPTIONS)  #displays options
    option_input_str = input("Enter one of the listed options: ")   #input
    option_input_str = option_input_str.lower()
    
    while not((option_input_str == 'a') or (option_input_str == 'b') or \
    (option_input_str == 'c') or (option_input_str == 'd') or \
    (option_input_str == 'q')):
        print('Invalid option!\nTry again')
        option_input_str = input("Enter one of the listed options: ")
        option_input_str = option_input_str.lower()
    
    return option_input_str

#prompts user to input a file name then trys to open the file and ensures 
#validity.

#this is used to generate a list that counts only a specific part of 
#each list in a list
def counting_list(master_list, index):
    #ensure no corruption of original master_list
    master_list_copy = copy.deepcopy(master_list)
    
    counting_list = []
    for song in master_list_copy:
        #append the part of the song at the index supplied
        counting_list.append(song[index])
    return counting_list

#takes the master_list, song, and index and returns a starting index and a
#list with the required spliced list section
def find_indicies_and_splice(master_list, song, index):
    master_list_copy = copy.deepcopy(master_list)

    count_list = counting_list(master_list_copy, index)
    
    #finds the index of the value we want in the count list which is the same 
    #as in the master_list
    index_start = count_list.index(song[index])
    
    count_list.reverse()   #reverses the list
    #finds the reverse index
    index_end_reversed = count_list.index(song[index])
    #takes the length - the index_reversed then takes the absolute value to 
    #find the ending index
    index_end = abs((len(count_list)) - index_end_reversed)
    
    #creates a splice list of the master_list using the given indicies
    splice_list = master_list_copy[index_start:index_end]
    
    #returns the starting index and the spliced list
    return index_start, splice_list

def open_file():
    try:
        file_name_input_str = input('Enter a file name: ')  #input file name
        song_data = open(file_name_input_str)   #opens the requested file
        return song_data   #returns the file pointer
    except FileNotFoundError:   #if the file is not found go to the while loop
        file_found = False
    while file_found == False:
        #try-except to ensure file is valid
        try:
            print('\nInvalid file name; please try again.\n')   
            file_name_input_str = input('Enter a file name: ')  #try again

            song_data = open(file_name_input_str)
            return song_data   #returns a file pointer
        except FileNotFoundError:   #loops until valid file is found
            file_found = False
   
def read_file(fp):   #creates the read_file function
    master_list = []   #intializes empty master_list
    
    #uses the csv reader module to turn opened file into a readable file.
    reader = csv.reader(fp)   
    next(reader)   #skips the headers
    for line in reader:   #reads each line
        #creates a list with the string values
        correct_types_list = [line[0], line[1]] 
        for element in line[2:]:   #now reads the rest of the values
            
            #try-except clause catches undefined values and sets equal to -1.
            try:
                element = int(element)
                if 100 >= element >= 0:   #catches any values that are invalid
                    correct_types_list.append(element)
                else:
                    correct_types_list.append(-1)
            except ValueError:
                correct_types_list.append(-1)
            
            #this ensures that the songs only have 6 elements associated with 
            #them one problem in testing was what happened if a song had extra
            #values associated so this was added to chop that off
            correct_types_list = correct_types_list[:6]
        #appends the list into a master list
        master_list.append(correct_types_list)
        
    
    
    fp.close()  #closing the file
    return master_list
    
def print_data(song_list):
    '''
    This function is provided to you. Do not change it
    It Prints a list of song lists.
    '''
    if not song_list:
        print("\nSong list is empty -- nothing to print.")
        return
    # String that the data will be formatted to. allocates space
    # and alignment of text
    format_string = "{:>3d}. "+"{:<45.40s} {:<20.18s} "+"{:>11d} "*4
    
    # Prints an empty line and the header formatted as the entries will be
    print()
    print(" "*5 + ("{:<45.40s} {:<20.18s} "+"{:>11.9s} "*4+'\n'+'-'*120)\
          .format(*TITLES))

    # Prints the formatted contents of every entry
    for i, sublist in enumerate(song_list, 1):
        #print(i,sublist)
        print(format_string.format(i, *sublist).replace('-1', '- '))

def get_christmas_songs(master_list):   #defines function get_christmas_songs
    
    #ensures master_list will not be changed
    master_list_copy = copy.deepcopy(master_list)  
    
    christmas_songs_list = []   #intializes an empty list
    for song in master_list_copy:   #reads each list in the master list
        title_str = song[0].lower()   #converts to lower case
        
        #for each phrase in the CHRISTMAS_WORDS collection, 
        #check if that phrase is in the title of the song
        for phrase in CHRISTMAS_WORDS:
            if phrase in title_str:
                #add the song to christmas_songs_list
                christmas_songs_list.append(song)
    
    #sort alphabetically and return the list
    sorted_christmas_songs_list = sorted(christmas_songs_list)
    return sorted_christmas_songs_list   

#function sorts by peak value. uses comprehension statement.
def sort_by_peak(master_list):
    #get each song from the master list then check that the peak value is not 
    #-1 and then sort based on the peak value.
    return sorted([i for i in master_list if not(i[4] == -1)], \
                  key=itemgetter(4))

#function sorts by weeks on the list. uses comprehension statement.
def sort_by_weeks_on_list(master_list):
    #copy to ensure no corruption
    master_list_copy = copy.deepcopy(master_list)
    index_alpha = 0
    for song in master_list_copy:
        
        #removes all songs that have a weeks_on value of -1
        if song[5] == -1:
            master_list_copy = master_list_copy[:index_alpha] + \
            master_list_copy[index_alpha+1:]
        index_alpha += 1
        
    #sorts by 5th index of each list of lists and then reverses
    master_list_copy = sorted(master_list_copy, key=itemgetter(5))
    master_list_copy.reverse()
    
    already_reverse = -1000
    index_beta = 5
    
    #makes a counting list
    count_list = counting_list(master_list_copy, 5)
    
    for song in master_list_copy:
         #checks if there is any ties for this value
         count = count_list.count(song[5])
         
         #only uses this tie breaker if it isn't repeating itself, to be more
         #efficient
         if count > 1 and not(already_reverse == song[5]):
            
            #uses the find_indicies_and_splice function to find the splice
            #and first index
            index_start, splice_list = \
            find_indicies_and_splice(master_list_copy, song, index_beta)
            
            #reverses it to keep in order it would originally be in
            splice_list.reverse()
            
            #adds the splice back in at its indicies
            for song_alpha in splice_list:
                master_list_copy[index_start] = song_alpha
                index_start += 1
            
            already_reverse = song[5]
             
    return master_list_copy
            
def song_score(song):   #defines the song_score function
    
    #creates a rank delta from the rank and previous rank
    rank_delta = song[2] - song[3]
    
    #if rank is -1 set the curr_rank to -100 otherwise set curr_rank 
    #to 100 - rank
    if song[2] == -1:
        curr_rank = -100
    else: 
        curr_rank = 100 - song[2]
    
    #does the same thing but with the peak rank
    if song[4] == -1:
        peak_rank = -100
    else:
        peak_rank = 100 - song[4]
    
    #use the song score equation to generate a score
    score = A*peak_rank + B*rank_delta + C*song[5] + D*curr_rank
    
    return score

def sort_by_score(master_list):
    #creates a copy to ensure master_list is not corrupted
    master_list_copy = copy.deepcopy(master_list)
    
    #assigns a score for each song
    for song in master_list_copy:
        score = song_score(song)
        song.append(score)
    
    #sorts by score
    master_list_copy = sorted(master_list_copy, key=itemgetter(6))
    master_list_copy.reverse()  #reverses
    
    #generates count list to for use in loop
    count_list = counting_list(master_list_copy, 6)
    already_reverse = -1000
    for song in master_list_copy:
         count = count_list.count(song[6])  #finds out if there is a tie
         
         #uses tiebreaker only if it has not been used prior for this value
         if count > 1 and not(already_reverse == song[6]):
            #uses the find indicies and splice function to find the necessary
            #splicing part and it first index
            index_start, splice_list = \
            find_indicies_and_splice(master_list_copy, song, 6)
            
            #this sorts alphabetically by title
            splice_list = sorted(splice_list)
            splice_list.reverse()   #reverse alphabetical order
            for song_alpha in splice_list:
                #this reads the songs in the reverse alhabetical order 
                #mutating the indexes that are already there
                master_list_copy[index_start] = song_alpha
                index_start += 1
            
            already_reverse = song[6]
    count = 0
    
    for song in master_list_copy:
        master_list_copy[count] = song[:6]  #cuts off the score for each song
        count += 1
    return master_list_copy

def main():
    print("\nBillboard Top 100\n")
    
    song_file = open_file()   #calls open_file()
    
    master_list = read_file(song_file)   #reads from the fp using read_file()
    
    print_data(master_list) #prints the data
    
    option_str = get_option()   #gets an option using get_option()
    
    while option_str != 'q':    #checks if the user wants to quit
        
        if option_str == 'a':   
            
            #call get_christmas_songs to get a list
            christmas_songs_list = get_christmas_songs(master_list)
            
            #divide the len of the christmas list by the len of the master 
            #list, multiply by 100 and then round by converting to int.
            christmas_song_float = int((len(christmas_songs_list)/\
                                        len(master_list))*100)
            
            print_data(christmas_songs_list)
            if christmas_song_float > 0:
                print('\n{:d}% of the top 100 songs are Christmas songs.'.\
                  format(christmas_song_float))
            else: 
                print('None of the top 100 songs are Christmas songs.')
                
        elif option_str == 'b':
            #use sort_by_peak function to sort the master_list
            peak_data_sorted_list = sort_by_peak(master_list)
            
            #use print_data function to print the sorted list
            print_data(peak_data_sorted_list)
        
        elif option_str == 'c':
            #use sort_by_weeks function to sort master list
            weeks_sorted_list = sort_by_weeks_on_list(master_list)
            
            #use print data function to print the sorted list
            print_data(weeks_sorted_list)
        
        elif option_str == 'd':
            #call the sort_by_score function to sort the master list
            song_score_sorted_list = sort_by_score(master_list)
            
            #print_data function to print the sorted list
            print_data(song_score_sorted_list)
        
        option_str = get_option()   #get another option and continue or quit

    print("\nThanks for using this program!\nHave a good day!\n")
    
# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()           