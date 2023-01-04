###############################################################################
#
# Computer Project #11
#
# Create a program which integrates the P11_Event class and the P11_Calendar 
# class into one program that creates a calendar of events. Can do the 
# following operations with the calendar:
#
# A - Add an event.
# D - Delete an event.
# L - List events for a given date.
# Q - Quit the Program.
#
# Has the following functions:
#
# check_time - Check that the time and duration inputted are for a valid time 
# frame.
#
# event_prompt - Prompt for date, time, duration, and meeting type, gathers 
# relevant information to add an event to calendar.
#
# main - Creates the calendar and then prompts for options for what to do 
# with it.
#
###############################################################################

from p11_calendar import P11_Calendar
from p11_event import P11_Event

CAL_TYPE = ['meeting','event','appointment','other']

OPTION_LIST = ['q', 'a', 'd', 'l']

MENU = '''Welcome to your own personal calender.
  Available options:
    (A)dd an event to calender
    (D)elete an event
    (L)ist the events of a particular date
    (Q)uit'''

def check_time(time,duration):
    """
    Checks that the time is between 6am and 5pm. Also checks if the duration
    is a valid integer greater than or equal to 1.
    time: The time string.
    duration: The duration integer.
    Returns: True or False depending on if the time and endtime are valid.
    """

    # Try to split into a list then isolate the hours and minutes. Check for 
    # validity. If invalid return False.
    try:
        time_list = time.split(':')
        hrs_int = int(time_list[0])
        mins_int = int(time_list[1])
        end_hrs = (duration // 60) + hrs_int
        end_mins = (duration % 60) + mins_int
        if end_mins > 59:
            end_hrs += end_mins // 60
            end_mins += end_mins % 60

        if hrs_int >= 6:
            if (end_hrs == 17) and (end_mins > 0):
                return False
            if end_hrs > 17:
                return False
        else:
            return False
    
    # Catches any errors that can occur when running the above program and if 
    # caught returns False.
    except (IndexError, ValueError, TypeError, AttributeError):
        return False
    
    # Checks the duration is an integer and greater than 1. Returns False if 
    # conditions not met.
    if (type(duration) == int) and (duration >= 1):
        None
    else:
        return False
    
    return True
            
def event_prompt():
    """
    Takes no parameters. Prompts for date, time, duration, and event type.
    Checks for validity of inputs and if invalid reprompts.
    Returns: The newly created event.
    """
    # Loop for error checking.
    while True:
        # Gather inputs.
        date_input = input('Enter a date (mm/dd/yyyy): ')
        time_input = input('Enter a start time (hh:mm): ')
        duration_input = input("Enter the duration in minutes (int): ")
        event_type_input = \
        input("Enter event type ['meeting','event','appointment','other']: ")
        # Try to convert duration to an integer if invalid do nothing the 
        # __init__ for events will catch it.
        try:
            duration_input = int(duration_input)
        except ValueError:
            None

        # Check if time and end time are valid, if they are then execute.
        if check_time(time_input, duration_input):
            # Initialize the event and if valid break the loop.
            new_event = P11_Event(date_input, time_input, duration_input, 
            event_type_input)
            if new_event.valid:
                break
        # If invalid repeat the loop and print the error message.
        print("Invalid event. Please try again.")

    return new_event

def main():
    # Initialize the calendar.
    calendar = P11_Calendar()

    # Run through the loop so that you can do multiple options.
    while True:
        # Display MENU.
        print(MENU)

        # Handle input option and error checking.
        option_str = input('Select an option: ')
        option_str = option_str.lower()
        while option_str not in OPTION_LIST:
            print("Invalid option. Please try again.")
            option_str = input('Select an option: ')
            option_str = option_str.lower()

        # Break the loop if option q.
        if option_str == 'q':
            break
        
        # Add an event if option a.
        elif option_str == 'a':
            # Prompt for the event.
            new_event = event_prompt()
            print("Add Event")
            # Add to calendar using add_event method.
            status = calendar.add_event(new_event) 

            # If status is completed print success message.
            if status:
                print("Event successfully added.")
            
            # If status is uncompleted print failure message.
            else:
                print("Event was not added.")

        # Delete an event if option d.
        elif option_str == 'd':
            print("Delete Event")

            # Prompt for date and time.
            date_input = input("Enter a date (mm/dd/yyyy): ")
            time_input = input('Enter a start time (hh:mm): ')

            # Call the delete event method with the date and time as args.
            status = calendar.delete_event(date_input, time_input)

            # If status is completed print success message.
            if status:
                print("Event successfully deleted.")
            
            # If status is uncompleted print failure message.
            else:
                print("Event was not deleted.")

        # List events for day if option l.
        elif option_str == 'l':
            print("List Events")
            # Get input for date.
            date_input = input("Enter a date (mm/dd/yyyy): ")
            # Call day_schedule method to get a sorted list of events for 
            # the day.
            day_list = calendar.day_schedule(date_input)

            # If events found print events.
            if day_list:
                for event in day_list:
                    print(event)

            # If no events print no events message.
            else:
                print("No events to list on  {}".format(date_input))

if __name__ == '__main__':
    main()