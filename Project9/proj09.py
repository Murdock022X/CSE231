###############################################################################
#
# Computer Project 9 CSE231
#
# Create a program that reads JSON files and then does the following functions.
#
# get_option()
# open_file()
# read_annot_file()
# read_category_file()
# collect_category_set()
# collect_img_list_for_categories()
# max_instances_for_item()
# max_images_for_item()
# count_words()
#
###############################################################################


import json, string
import string
from operator import itemgetter

STOP_WORDS = ['a', 'an', 'the', 'in', 'on', 'of', 'is', 'was', 'am', 'I', 
            'me', 'you', 'and', 'or', 'not', 'this', 'that', 'to', 'with',
            'his', 'hers', 'out', 'it', 'as', 'by', 'are', 'he', 'her', 
            'at', 'its']

MENU = '''
    Select from the menu:
        c: display categories
        f: find images by category
        i: find max instances of categories
        m: find max number of images of categories
        w: display the top ten words in captions
        q: quit

    Choice: '''


def get_option():
    """
    Get's a valid string option.

    :rtype: Str
    :return: option_input_str, a character in cfimwq.
    """
    while True:   # Loop until valid input is found.

        try:
            # Print the menu and take input string. Convert to lowercase.
            option_input_str = (input(MENU)).lower()

        # If not correct type try again and catch with except.
        except ValueError:
            print("Incorrect choice.  Please try again.")
            continue

        # If the letter is not a valid option don't accept it.
        if option_input_str not in 'cfimwq':
            print("Incorrect choice.  Please try again.")
            continue

        else:
            return option_input_str


def open_file(s):
    """ Open a JSON file pointer and category/image classifier.txt file. 
    Error checking included. """

    # Run until value returned.
    while True:
        # Get a file string.
        fp_str = input("Enter a {} file name: ".format(s))
        
        # Try to open the file, catch it with FileNotFoundError if faulty. 
        try:
            fp = open(fp_str)
            return fp
        except FileNotFoundError:
            print("File not found.  Try again.")


def read_annot_file(fp1):
    """
    Loads the JSON file.
    :param fp1: JSON file pointer
    :type fp1: file-pointer
    :rtype: Dictionary
    :return: JSON Dictionary
    """
    return json.load(fp1)


def read_category_file(fp2):
    """
    Create a dictionary from the fp2 file to create a way to classify objects.
    :param fp2: category file pointer
    :type: fp2
    :rtype: dictionary
    :return: classifier_dict
    """

    classifier_dict = {}   # Intialize dictionary.

    for line in fp2:   # Read each line in file.
        line_list = line.split()   # Create a list of each word.
        line_list[0] = int(line_list[0]) # Convert the number to an int.

        # Create the new dict value in the classifier with the int as the key
        # and the category the number refers to as the value.
        classifier_dict[line_list[0]] = line_list[1]

    return classifier_dict


def collect_catogory_set(D_annot, D_cat):
    """
    Collects all the categories in the image from the annot dictionary into
    a set. Then takes the set and matches to the corresponding words from 
    the category dictionary.

    :param D_annot: The dictionary with the image annotations.
    :type D_annot: Dictionary
    :param D_cat: The category dictionary.
    :type D_cat: Dictionary
    :rtype: Set
    :return cat_str_set: A set of strings that tell what are in the image.
    """

    cat_num_set = set()   # Intialize the set.
    for image in D_annot.values():   # Go through each image in the dictioary.
        # Iterate through each category int in the bbox_category_label list and
        # add it into the set.
        for cat_int in image['bbox_category_label']:
            cat_num_set.add(cat_int)

    cat_str_set = set()   # Intialize the set.

    # For each number in the the cat_num_set get the word value of it from the
    # category dictionary and then add that into a new set
    for num in cat_num_set:
        cat_str = D_cat[num]
        cat_str_set.add(cat_str)

    return cat_str_set


def collect_img_list_for_categories(D_annot, D_cat, cat_set):
    """
    Creates a dictionary with the item as the key and the image(s) it appears
    in as a list that is the value.

    :param D_annot: The dictionary returned by the JSON file.
    :type D_annot: Dictionary

    :param D_cat: The category dictionary with item numbers as keys and 
    the item strings as values.
    :type D_cat: Dictioary

    :param cat_set: The set of category's appearing in the images.
    :type cat_set: Set

    :rtype: Dictionary
    :return: item_images_dict, the dictionary with the item as the key and the
    images as the value.
    """

    # Dictionary comprehension to create empty lists for each element in the 
    # category set.
    item_images_dict = {element:[] for element in cat_set}

    # Iterate through each image getting the image id and the sub-dictionary.
    for image_id, json_dict in D_annot.items():
        cat_str_set = set()

        # For each category label in the dictionary get the categiry that it
        # is, then put the image id in the dictionary entry for that item.
        for cat_label in json_dict['bbox_category_label']:
            cat_str = D_cat[cat_label]
            item_images_dict[cat_str].append(int(image_id))

    for img_list in item_images_dict.values():
        img_list.sort()
        for i, img_id in enumerate(img_list):
            img_list[i] = str(img_id)

    return item_images_dict


def max_instances_for_item(D_image):
    """
    Returns a tuple that is the number of times an item appears in all the 
    images.
    :param D_image: The dictionary with the items as keys and the images they
    are in as list values. See collect_img_list_for_categories function.
    :type D_image: Dictionary
    :rtype: Tuple
    :return: Returns a tuple with the number of times an item appears in all
    the images.
    """

    # Comprehension iterates through each item in the D_image dict and gets
    # the number of times it appears and what it is. Then it takes the
    # maximum.
    return max([(len(img_list), item) for item, img_list in D_image.items()])


def max_images_for_item(D_image):
    """
    Returns a tuple that is the number of images an item appears in and the 
    item.
    :param D_image: The dictionary with the items as keys and the images they
    are in as list values. See collect_img_list_for_categories function.
    :type D_image: Dictionary
    :rtype: Tuple
    :return: Returns a tuple with the number of images an item appears in and
    the item.
    """

    # Comprehension iterates through each item in the D_image dict and gets
    # the number of images it appears in and what it is. Then it takes the
    # maximum.
    return \
    max([(len(set(img_list)), item) for item, img_list in D_image.items()])


def count_words(D_annot):
    """
    Counts the number of times a caption word appears. Disregards
    irrelevant words.
    :param D_annot: The dictionary generated by the JSON loading.
    :type D_annot: Dictionary
    :rtype: List of tuples
    :return: The list of tuples of words and the number of times they appear.
    """
    words_dict = {}   # Intialize a dictionary.
    for img_dict in D_annot.values():   # Iterate through D_annot dictionarys.

        # Iterate through captions in the cap_list.
        for caption in img_dict['cap_list']:

            # Split into a list of words.
            word_list = caption.split()

            # Iterate through each word in the list.
            for word in word_list:

                # Strip of punctuation.
                word = word.strip(string.punctuation)

                # Don't include unimportant words.
                if word in STOP_WORDS:
                    continue

                # If not in the keys set the new value to 1.
                elif word not in words_dict.keys():
                    words_dict[word] = 1
                
                # If word in keys add one to the occurence value.
                elif word in words_dict.keys():
                    words_dict[word] = words_dict[word] + 1

    # Create a list of words and occurences in tuples.
    words_list = [(occur_int, word) for word, occur_int in words_dict.items()]

    # Sort them reverse alphabetically.
    words_list.sort(key=itemgetter(1), reverse=True)

    # Sort by occurence.
    words_list.sort(reverse=True)

    return words_list

def main():
    print("Images\n")
    fp1 = open_file('JSON image')   # Open the JSON file pointer.
    annot_dict = read_annot_file(fp1)   # Load the JSON dictionary.

    fp2 = open_file('category')   # Open the category txt file pointer.
    cat_dict = read_category_file(fp2)   # Read into a dictionary.

    # Create the category set.
    cat_set = collect_catogory_set(annot_dict, cat_dict)

    # Create the dictionary with categories as keys and a list of image id's
    # they appear in as values.
    img_list_dict = collect_img_list_for_categories( \
        annot_dict, cat_dict, cat_set)

    choice_input_str = get_option()   # Get an option to decide what to do.
    while not(choice_input_str == 'q'):
        
        # If user wants to see the categories.
        if choice_input_str == 'c':
            print("\nCategories:")
            cat_list = list(cat_set)
            cat_list.sort()

            # Create a string with correct formatting.
            whole_cat_str = ''
            for index, cat_str in enumerate(cat_list):
                if index != (len(cat_list) -1):
                    whole_cat_str += cat_str + ', '
                else:
                    whole_cat_str += cat_str
            print(whole_cat_str)
        
        # If user wants to see categories, then see what images category
        # appears in.
        elif choice_input_str == 'f':

            print("\nCategories:")
            # Convert cat_set to a list so that it is an orderedsequence and
            # sortable.
            cat_list = list(cat_set)
            cat_list.sort()

            # Generate a string to display.
            whole_cat_str = ''
            for index, cat_str in enumerate(cat_list):
                # Include comma unless last element.
                if index != (len(cat_list) -1):
                    whole_cat_str += cat_str + ', '
                else:
                    whole_cat_str += cat_str
            print(whole_cat_str)

            # Get a category, run until valid category selected.
            while True:
                cat_input_str = input("Choose a category from the list above: ")

                # Try, except to catch KeyErrors.
                try:
                    # Due to conversion to a set and back to a list here, which
                    # eliminates duplicate image_id's, image id's must be 
                    # converted back to ints for sorting. Function test in 
                    # mirmir for collect_img_list_for_categories demanded 
                    # sorted lists with strings.
                    img_list = list(set(img_list_dict[cat_input_str]))
                    for i,img_id in enumerate(img_list):
                        img_list[i] = int(img_id)
                    img_list.sort()
                    break
                except KeyError:
                    print("Incorrect category choice.")

            print("\nThe category {} appears in the following images:".
            format(cat_input_str))

            # Generate a string with all the image id's in order.
            whole_img_str = ''
            for index, img_str in enumerate(img_list):
                if index != (len(img_list) - 1):
                    whole_img_str += str(img_str) + ', '
                else:
                    whole_img_str += str(img_str)
            
            print(whole_img_str)

        # Choice for max number of times something appears in all images.
        elif choice_input_str == 'i':
            # Call the max_instances function to get the tuple, then display.
            max_instances_tup = max_instances_for_item(img_list_dict)
            print(
                "\nMax instances: the category {} appears {} times in images.".
                format(max_instances_tup[1], max_instances_tup[0]))

        # Choice for max number of images something appears in.
        elif choice_input_str == 'm':
            # Call the max_images function to get the tuple, then display.
            max_images_tup = max_images_for_item(img_list_dict)
            print(
                "\nMax images: the category {} appears in {} images.".
                format(max_images_tup[1], max_images_tup[0]))
        
        # If user wants to show captions and they're occurences.
        elif choice_input_str == 'w':
            # Gets a valid input for the number of words to display.
            while True:
                # Try except catches wrong types.
                try:
                    words_input_int = int(input(
                        "\nEnter number of desired words: "))
                except ValueError:
                    print("Error: input must be a positive integer: ")
                
                # If statement catches numbers less than 0.
                if words_input_int > 0:
                    break
                else:
                    print("Error: input must be a positive integer: ")
            
            # Call the count words function to get the list of tuples.
            words_list_of_tups = count_words(annot_dict)
            
            # Print headers then iterate through display words and occurences.
            print("\nTop {} words in captions.".format(words_input_int))
            print("{:<14s}{:>6s}".format("word","count"))
            for tups in words_list_of_tups[:words_input_int]:
                print("{:<14s}{:>6d}".format(tups[1], tups[0]))
        
        # Get a new option.
        choice_input_str = get_option()

    print("\nThank you for running my code.")


# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()