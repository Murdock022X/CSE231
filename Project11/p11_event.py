###############################################################################
#
# Computer Project #11
#
# Creates the P11_event class.
# Has the following methods:
#
# __init__ - Initializes the time, date, duration, cal_type, and valid 
# attributes.
# get_date - Returns the date attribute.
# get_time - Returns the time attribute.
# get_time_range - Returns a tuple with the start and end times of an event.
# __str__ - Returns a string with date followed by time and duration.
# __repr__ - Creates a string with one event followed by another.
# __lt__ - Checks events time is less than the other events time.
# __eq__ - Checks if date, time, and duration are equal.
#
###############################################################################



CAL_TYPE = ['meeting','event','appointment','other']

class P11_Event(object):
    def __init__(self,date=None,time='9:00',duration=60,cal_type='meeting'):
        """
        Initializes an event. Returns public attributes date, time, 
        duration, cal_type, and valid. Valid will be True if all other 
        inputs are valid, False if otherwise.

        self: The event being intialized.
        date: The date the event is on.
        time: The start time for the event.
        duration: The length of the event.
        cal_type: The type of event.
        """
        
        # Try to split into a list then isolate the hours and minutes. Check 
        # for validity and if valid create a string. Otherwise make the time 
        # variable None.
        try:
            time_list = time.split(':')
            hrs_int = int(time_list[0])
            mins_int = int(time_list[1])

            if (0 <= hrs_int <= 23) and (0 <= mins_int <= 59):
                time_str = '{}:{:<02}'.format(hrs_int, mins_int)
            else:
                time_str = None
        
        # Catches any errors that can occur when running the above program 
        # and if caught sets the time variable to None.
        except (IndexError, ValueError, TypeError, AttributeError):
            time_str = None

        # Generate the public time attribute.
        finally:
            self.time = time_str

        # Try to split into a list then isolate months, days, and years. 
        # Check for validity and if valid create a string. Otherwise make 
        # the time variable None.
        try:
            date_list = date.split('/')
            mth_int = int(date_list[0])
            day_int = int(date_list[1])
            yr_int = int(date_list[2])

            if (1 <= mth_int <= 12) and (1 <= day_int <= 31) and \
            (0 <= yr_int <= 9999):
                date_str = '{}/{}/{}'.format(mth_int, day_int, yr_int)
            else:
                date_str = None
        
        # If any of these errors occur set the date variable to None.
        except (IndexError, ValueError, TypeError, AttributeError):
            date_str = None
        
        # Generate the public date attribute.
        finally:
            self.date = date_str

        # If a valid duration is supplied set the public duration attribute 
        # equal to it. Otherwise set equal to None.
        if (type(duration) == int) and (duration >= 1):
            self.duration = duration
        else:
            self.duration = None

        # Check that the cal_type is in CAL_TYPE, if it is set the public 
        # cal_type attribute equal to it. Otherwise set it equal to None.
        if cal_type in CAL_TYPE:
            self.cal_type = cal_type
        else:
            self.cal_type = None

        # If any of these are set equal to None and therefore invalid set the 
        # valid attribute to False, otherwise set to True.
        if self.cal_type == None:
            self.valid = False
        elif self.time == None:
            self.valid = False
        elif self.date == None:
            self.valid = False
        elif self.duration == None:
            self.valid = False
        else:
            self.valid = True
 
    def get_date(self):
        """
        Returns the date string. Takes no arguments besides self.
        self: The event to retreive the date from.
        Returns: The date string.
        """
        return self.date

    def get_time(self):
        """
        Returns the time string. Takes no arguments besides self.
        self: The event to retreive the time from.
        Returns: The time string.
        """
        return self.time

    def get_time_range(self):
        """
        Checks the time of the event and the duration to generate an end 
        time. Returns a tuple with start time and then end time.
        self: The event to get the range from.
        Returns: A tuple with the start time followed by end time.
        """
        
        # Retrieve the time and duration.
        start_time = self.get_time()
        duration_int = self.duration

        # Split the time into component parts.
        start_time_list = start_time.split(':')

        # Calculate start time in minutes.
        start_mins = (int(start_time_list[0]))*60 + int(start_time_list[1])

        # Add duration to get the end time.
        end_mins = start_mins + duration_int

        return (start_mins, end_mins)
    
    def __str__(self):
        """
        Returns a string with the date followed by the time and duration. 
        Takes self as an argument.
        self: The event.
        Returns: The string with the date, time, and duration.
        """

        date = self.get_date()
        time = self.get_time()
        return '{}: start: {}; duration: {}'.format(date, time, self.duration)
    
    def __repr__(self):
        '''PROVIDED'''
        if self.date and self.time and self.duration:
            return self.date + ';' + self.time + '+' + str(self.duration)
        else:
            return 'None'

    def __lt__(self,e):
        """
        Checks if self is less than the other event by converting to minutes
        and comparing the integers.
        self: The event.
        e: Another event to compare to.
        Returns: True or False depending on whether the self events time is 
        less than e events time.
        """
        # Get the self time and if None return False.
        time1 = self.get_time()
        if not time1:
            return False

        # Split into parts and convert hours to minutes.
        time1_list = time1.split(':')
        time1_mins = int(time1_list[0])*60 + int(time1_list[1])

        # Get the self time and if None return False.
        time2 = e.get_time()
        if not time2:
            return False
        
        # Split into parts and convert hours to minutes.
        time2_list = time2.split(':')
        time2_mins = int(time2_list[0])*60 + int(time2_list[1])

        # Return True if e's time is greater than self's time. Return False 
        # otherwise.
        if time1_mins < time2_mins:
            return True
        else:
            return False
        
    
    def __eq__(self,e):
        '''PROVIDED'''
        return self.date == e.date and self.time == e.time and \
        self.duration == e.duration and \
        self.cal_type == e.cal_type # and self.status == e.status