###############################################################################
#
# Computer Project #11
#
# p11_calendar module
#
# Creates the P11_Calendar class.
# Has the following methods:
# 
# __init__ - Intialize the calendar event_list attribute.
# add_event - Add an event to the calendar event list.
# delete_event - Delete an event from the event list.
# day_schedule - Shows the events for the specified date.
# __str__ - Returns a string with all the events in the calendar.
# __repr__ - Creates a string of all the events in a line.
# __eq__ - Checks the equivalence of two calendars.
#
###############################################################################


class P11_Calendar():
    def __init__(self):
        """Initialize the calendar to an empty list.
        self: The variable to be intialized to the calendar.
        """
        self.event_list = []
        
    def add_event(self,e):
        """Adds an event to the calendars event list.
        self: The calendar being operated on.
        e: The event to be added.
        Returns: True or False depending on if the operation was completed.
        """

        # Gets the time range for the event.
        e_times_tup = e.get_time_range()

        # Iterates through each event in the event list.
        for event in self.event_list:
            # Checks if the date is the same.
            if event.get_date() == e.get_date():
                # Gets this events time range.
                event_times_tup = event.get_time_range()

                # Checks whether there is any overlap between event times by 
                # checking start and end times. Returns False if there is.
                if event_times_tup[0] > e_times_tup[0]:
                    if event_times_tup[0] < e_times_tup[1]:
                        return False

                # Checks whether there is any overlap between event times by 
                # checking start and end times. Returns False if there is.
                elif event_times_tup[0] < e_times_tup[0]:
                    if event_times_tup[1] > e_times_tup[0]:
                        return False
        
        # If there are no conflicts the event is appended and the method 
        # returns True.
        self.event_list.append(e)
        return True
    
    def delete_event(self,date,time):
        '''Finds an event at the date and time and then deletes it from the 
        calendars event list.'''
        index = 0   # Intializes the index to 0.

        # Iterates through each event in the event list.
        for event in self.event_list:
            # Checks if the date is the same.
            if event.get_date() == date:
                # Checks if the time is the same. If it is then break.
                if event.get_time() == time:
                    break

            index += 1   # Increase the index by 1.

        # If the for loop finds no events matching it returns False.
        if index == len(self.event_list):
            return False
        
        # Deletes the event from the event list using the del command and the 
        # index obtained. Returns True.
        del self.event_list[index]
        return True

    def day_schedule(self,date):
        '''Creates a schedule for a specified date. Arranges it in order by 
        time. Returns the day in the list type.'''

        # If the event list is empty return False.
        if not self.event_list:
            return False
        
        # Try to check that the date is valid and properly formatted.
        try:
            date_list = date.split('/')
            mth_int = int(date_list[0])
            day_int = int(date_list[1])
            yr_int = int(date_list[2])

            # Checks the 
            if (1 <= mth_int <= 12) and (1 <= day_int <= 31) and \
            (0 <= yr_int <= 9999):
                date_str = '{}/{}/{}'.format(mth_int, day_int, yr_int)
            else:
                return False
        
        # If any of these errors occur return None.
        except (IndexError, ValueError, TypeError, AttributeError):
            return False

        # List comprehension, events added if on cooresponding day, 
        # then sorted.
        return sorted(\
            [event for event in self.event_list if event.get_date() == date])

    def __str__(self):
        '''Generates a string with a header and all the events in the 
        calendar.'''
        return_str = 'Events in Calendar:\n'

        # Iterates throught the list adding each event to the string as 
        # it goes.
        for event in self.event_list:
            return_str += '{}: start: {}; duration: {}\n'.\
            format(event.get_date(), event.get_time(), event.duration)
        
        return return_str
    
    def __repr__(self):
        '''PROVIDED'''
        s = ''
        for e in self.event_list:
            s += e.__repr__() + ";"
        return s[:-1]
    
    def __eq__(self,cal):
        '''PROVIDED: returns True if all events are the same.'''
        if not isinstance(cal,P11_Calendar):
            return False
        if len(self.event_list) != len(cal.event_list):
            return False
        L_self = sorted(self.event_list)
        L_e = sorted(cal.event_list)
        for i,e in enumerate(L_self):
            if e != L_e[i]:
                return False
        return True
        