#####################################################################
#
# Computer Project #8
#
# Create a dictionary of lists of diabetes data for countries.
#
# Create functions that find the minimum and maximum per
# capita diabetes value in each region.
#
# Create a function that finds the per capita diabetes value
# for each country.
#
# Create a function that displays the data.
#
#####################################################################


import csv
from operator import itemgetter


def open_file():
    """
    Generates a file pointer. Uses error checking.
    :rtype: file-pointer
    :return: fp
    """

    file_name_str = input("Input a file: ")

    while True:  # Runs for loop until file is found.
        try:
            # Generates the file-pointer using utf-8 encoding.
            fp = open(file_name_str, encoding='utf-8')
            return fp
        # Generate error if not found.
        except FileNotFoundError:
            print("Error: file does not exist. Please try again.")
            file_name_str = input("Input a file: ")


def max_in_region(D, region):
    """
    Finds the maximum per capita diabetes value in the selected region.
    @param D: The dict of lists containing the countries data.
    @param region: The inputted region, used to get the relevant dict entry.
    @return: Returns the maximum value and the country name in a tuple.
    """
    # List comprehension to create tuples with country name and per-capita
    # values.
    list_of_per_capita_values = \
        [(country_list[0], country_list[3]) for country_list in D[region] if country_list[3] != 0.0]

    # Find the maximum per-capita and return that tuple.
    return max(list_of_per_capita_values, key=itemgetter(1))


def min_in_region(D, region):
    """
    Finds the minimum per capita diabetes value in the selected region.
    @param D: The dict of lists containing the countries data.
    @param region: The inputted region, used to get the relevant dict entry.
    @return: Returns the minimum value and the country name in a tuple.
    """
    # List comprehension to generate tuples of country name and
    # per-capita values.
    list_of_per_capita_values = \
        [(country_list[0], country_list[3]) for country_list in D[region] if country_list[3] != 0.0]

    # Finds the minimum per-capita value and returns that tuple.
    return min(list_of_per_capita_values, key=itemgetter(1))


def read_file(fp):
    """
    Reads the file pointer using the csv reader. Reads it into a dictionary
    list of lists. Uses region as key and has a list of lists where each list
    is a country's values.
    @param fp: The file pointer to read from.
    @return: Returns the dictionary list of lists.
    """
    reader = csv.reader(fp)  # Generate a reader for the csv file.
    next(reader)
    dict_of_lists = {}  # Intialize the dict of lists.

    # Iterate through each line in reader/csv file.
    for line in reader:

        # Try to convert to floats and ints. If they cannot be converted,
        # it because it is empty, so this handles error_checking and
        # conversion.
        try:
            line[5] = line[5].replace(',', "")
            line[5] = float(line[5])
            line[9] = float(line[9])

        # If there is a problem converting skip past the line.
        except ValueError:
            continue

        # If the region is already in the dict execute.
        if line[1] in dict_of_lists.keys():
            # Generate a country_list with country name, pop, and cases.
            country_list = [line[2], line[9], line[5]]

            # Append to the regional list.
            dict_of_lists[line[1]].append(country_list)

        # If the region is not in the dict yet, execute.
        if not (line[1] in dict_of_lists.keys()):
            # Create a new dict entry with the region as the key, and a
            # list of lists with the country name, pop, and cases as the
            # first list.
            dict_of_lists[line[1]] = [[line[2], line[9], line[5]]]

    # Sort all the lists.
    for list_of_lists in dict_of_lists.values():
        list_of_lists = list_of_lists.sort()

    return dict_of_lists


def add_per_capita(D):
    """
    Appends the per capita diabetes value to each country's list.
    (Diabetes value/population).
    @param D: The dict of lists.
    @return: Return the dict of lists
    """

    # Iterates through the keys and values of the dictionary.
    for region, list_of_lists in D.items():

        # Iterates through the list of lists.
        for country_list in list_of_lists:

            # Try to divide the case numbers by the population numbers.
            # Append the value to the end of the countries list. If division
            # by zero occurs, simply append 0.0.
            try:
                diabetes_per_capita = country_list[1] / country_list[2]
                country_list.append(diabetes_per_capita)
            except ZeroDivisionError:
                country_list.append(0.0)

    return D


def display_region(D, region):
    """
    Displays a summary of each country in the region, as well as the regional
    summary.
    @param D: Dict of lists of lists. Each big list is a region. Each list
    inside is a country's data.
    @param region: The region that should be printed.
    """

    # Finds the regional maximum and minimum per-capita values using the
    # respective functions.
    regional_max_tup = max_in_region(D, region)
    regional_min_tup = min_in_region(D, region)

    # Iterate through each country_list in the regional list of lists.
    list_of_country_lists = []
    for country_list in D[region]:

        # Finds the summary data for the region and isolates it and removes it.
        if country_list[0] == region:
            regional_totals_list = country_list

        else:
            list_of_country_lists.append(country_list)

    list_of_country_lists = sorted(list_of_country_lists, key=itemgetter(3), reverse=True)

    # Print headers.
    print("Type1 Diabetes Data (in thousands)")
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Region", "Cases",
                                                  "Population", "Per Capita"))

    # Print the regional summary.
    print("{:<37s} {:>9.0f} {:>12,.0f} {:>11.5f}"
          .format(region, regional_totals_list[1], regional_totals_list[2],
                  regional_totals_list[3]))

    # More headers.
    print("{:<37s} {:>9s} {:>12s} {:>11s}"
          .format("Country", "Cases", "Population", "Per Capita"))

    # Iterate through each country_list in the regional list of lists and print
    # country name, pop, cases, and per-capita values.
    for country_list in list_of_country_lists:
        print("{:<37s} {:>9.1f} {:>12,.0f} {:>11.5f}".format(country_list[0],
                                                             country_list[1],
                                                             country_list[2],
                                                             country_list[3]))

    # Prints the maximum per-capita and minimum per-capita values for the
    # region.
    print("\nMaximum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country", "Per Capita"))
    print("{:<37s} {:>11.5f}".format(regional_max_tup[0], regional_max_tup[1]))

    print("\nMinimum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country", "Per Capita"))
    print("{:<37s} {:>11.5f}\n".format(regional_min_tup[0], regional_min_tup[1]))
    print("-" * 72)


def main():
    fp = open_file()  # Open the file.
    master_dict = read_file(fp)  # Read the file into a dictionary.
    master_dict = add_per_capita(master_dict)   # Add on the per_capita values.

    # Iterate through each region in the dictionary.
    for region in master_dict.keys():
        # Call the display function to print.
        display_region(master_dict, region)

    print('\nThanks for using this program!\nHave a good day!')


# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()
