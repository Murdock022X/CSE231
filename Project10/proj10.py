###############################################################################
# 
# Computer Project CSE231 10
#
# Create a program that plays Streets and Alleys solitaire game.
#
# Intialize()
#
# display()
#
# valid_tableau_to_tableau()
# move_tableau_to_tableau()
#
# valid_foundation_to_tableau()
# move_foundation_to_tableau()
#
# valid_tableau_to_foundation()
# move_tableau_to_foundation()
#
# check_for_win()
#
# get_option()
#
# main()
#
###############################################################################


#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from Tableau pile s to Tableau pile d.
    MTF s d: Move card from Tableau pile s to Foundation d.
    MFT s d: Move card from Foundation s to Tableau pile d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''
                
def initialize():
    """
    Creates the foundation list of lists and the tableau list of lists.
    Deals left to right.

    :rtype: Two lists of lists
    :return: Returns the foundation list of lists and the tableau
    list of lists.
    """
    alpha_deck = cards.Deck()   # Creates the deck for dealing.

    # Creates the empty foundation list with four empty lists.
    foundation_list = [[],[],[],[]]

    # Creates an empty tableau list of 8 empty lists.
    tableau_list = [[],[],[],[],[],[],[],[]]
    alpha_deck.shuffle()   # Shuffle
    
    # Iterates 52 times i.e each card in deck.
    for i in range(52):
        # Calls the deal method to pop the card and remove it from the deck.
        card = alpha_deck.deal()

        # Cascading list of if statements to deal the right 
        # number of cards to each deck.
        if len(tableau_list[0]) != 7:
            tableau_list[0].append(card)
            continue
        elif len(tableau_list[1]) != 6:
            tableau_list[1].append(card)
            continue
        elif len(tableau_list[2]) != 7:
            tableau_list[2].append(card)
            continue
        elif len(tableau_list[3]) != 6:
            tableau_list[3].append(card)
            continue
        elif len(tableau_list[4]) != 7:
            tableau_list[4].append(card)
            continue
        elif len(tableau_list[5]) != 6:
            tableau_list[5].append(card)
            continue
        elif len(tableau_list[6]) != 7:
            tableau_list[6].append(card)
            continue
        elif len(tableau_list[7]) != 6:
            tableau_list[7].append(card)
            continue

    return tableau_list, foundation_list

def display(tableau, foundation):
    '''Each row of the display will have
       tableau - foundation - tableau
       Initially, even indexed tableaus have 7 cards; odds 6.
       The challenge is the get the left vertical bars
       to line up no matter the lengths of the even indexed piles.'''
    
    # To get the left bars to line up we need to
    # find the length of the longest even-indexed tableau list,
    #     i.e. those in the first, leftmost column
    # The "4*" accounts for a card plus 1 space having a width of 4
    max_tab = 4*max([len(lst) for i,lst in enumerate(tableau) if i%2==0])
    # display header
    print("{1:>{0}s} | {2} | {3}".format(max_tab+2,"Tableau","Foundation","Tableau"))
    # display tableau | foundation | tableau
    for i in range(4):
        left_lst = tableau[2*i] # even index
        right_lst = tableau[2*i + 1] # odd index
        # first build a string so we can format the even-index pile
        s = ''
        s += "{}: ".format(2*i)  # index
        for c in left_lst:  # cards in even-indexed pile
            s += "{} ".format(c)
        # display the even-indexed cards; the "+3" is for the index, colon and space
        # the "{1:<{0}s}" format allows us to incorporate the max_tab as the width
        # so the first vertical-bar lines up
        print("{1:<{0}s}".format(max_tab+3,s),end='')
        # next print the foundation
        # get foundation value or space if empty
        found = str(foundation[i][-1]) if foundation[i] else ' '
        print("|{:^12s}|".format(found),end="")
        # print the odd-indexed pile
        print("{:d}: ".format(2*i+1),end="") 
        for c in right_lst:
            print("{} ".format(c),end="") 
        print()  # end of line
    print()
    print("-"*80)
          
def valid_tableau_to_tableau(tableau,s,d):
    """
    Checks the validity of a move from one tableau pile to another.
    
    :param tableau: The tableau list of lists.
    :type tableau: List of lists

    :param s: The source tableau pile index.
    :type s: Int

    :param d: The destination tableau pile index.
    :type d: Int

    :rtype: bool
    :return: True if move valid, False if move invalid.
    """

    # Check if the length of tableau pile is greater than or equal to 1.
    # If it is generate the source card.
    if len(tableau[s]) >= 1:
        source_card = tableau[s][len(tableau[s]) - 1]

    # Otherwise return false as their is no source card.
    elif not tableau[s]:
        return False

    # Check if there is a card in the pile. Then generate the 
    # destination card if valid.
    if len(tableau[d]) >= 1:
        destination_card = tableau[d][len(tableau[d]) - 1]
    
    # If the pile is empty return True as any card can be moved to an empty
    # tableau.
    elif not tableau[d]:
        return True

    # If the rank of the source card being moved is one less than the 
    # destination card then return True. Otherwise return False.
    if (source_card.rank() + 1) == destination_card.rank():
        return True
    else:
        return False
    
def move_tableau_to_tableau(tableau, s, d, undo_bool=False):
    """
    Moves a card from a tableau to a tableau as specified if valid. A 
    modification was made to the functions parameters. Undo_bool allows 
    the function to skip move validation if set as True. This allows the 
    program to execute normally illegal undo moves.

    :param tableau: The tableau list of lists.
    :type tableau: List of lists.

    :param s: The source pile index.
    :type s: Int

    :param d: The destination pile index.
    :type d: Int

    :rtype: bool
    :return: True or False depending on if a valid move.
    """

    # Check if a valid move then pop the last card from the relevant pile
    # then append to the correct pile. Return True if valid. If undo bool set
    # to true, run anyway. Allows illegal undo moves.
    if valid_tableau_to_tableau(tableau, s, d) or undo_bool:
        source_card = tableau[s].pop()
        tableau[d].append(source_card)
        return True
    
    else:
        return False

def valid_foundation_to_tableau(tableau,foundation,s,d):
    """
    Checks the validity of a move from a foundation pile to a tableau pile.
    
    :param tableau: The tableau list of lists.
    :type tableau: List of lists

    :param foundation: The foundation list of lists.
    :type foundation: List of lists

    :param s: The source foundation pile index.
    :type s: Int

    :param d: The destination tableau pile index.
    :type d: Int

    :rtype: bool
    :return: True if move valid, False if move invalid.
    """

    # Check if the length of foundation pile is greater than or equal to 1. 
    # If it is generate the source card.
    if len(foundation[s]) >= 1:
        source_card = foundation[s][len(foundation[s]) - 1]
    
    # Otherwise return false as their is no source card.
    elif not foundation[s]:
        return False

    # Check if there is a card in the pile. Then generate the 
    # destination card if valid.
    if len(tableau[d]) >= 1:
        destination_card = tableau[d][len(tableau[d]) - 1]
    
    # If the pile is empty return True as any card can be moved to an empty
    # tableau.
    elif not tableau[d]:
        return True

    # If the rank of the source card being moved is one less than the 
    # destination card then return True. Otherwise return False.
    if (source_card.rank() + 1) == destination_card.rank():
        return True
    else:
        return False

def move_foundation_to_tableau(tableau,foundation,s,d, undo_bool=False):
    """
    Moves the foundation card to the tableau as specified and if valid. A 
    modification was made to the functions parameters. Undo_bool allows 
    the function to skip move validation if set as True. This allows the 
    program to execute normally illegal undo moves.

    :param tableau: The tableau list of lists.
    :type tableau: List of lists

    :param foundation: The foundation list of lists.
    :type foundation: List of lists

    :param s: The source foundation pile index.
    :type s: Int

    :param d: The destination tableau pile index.
    :type d: Int

    :rtype: bool
    :return: True or False depending on if a valid move.
    """

    # Check if a valid move, if valid pop the relevant card and then append
    # the card to the relevant pile. Return True if completed otherwise
    # return False. If undo_bool set to execute without validation for move.
    # Allows illegal undo moves.
    if valid_foundation_to_tableau(tableau, foundation, s, d) or undo_bool:
        source_card = foundation[s].pop()
        tableau[d].append(source_card)
        return True
    
    else:
        return False

def valid_tableau_to_foundation(tableau,foundation,s,d):
    """
    Checks the validity of a move from a tableau pile to a foundation pile.
    
    :param tableau: The tableau list of lists.
    :type tableau: List of lists

    :param foundation: The foundation list of lists.
    :type foundation: List of lists

    :param s: The source foundation pile index.
    :type s: Int

    :param d: The destination tableau pile index.
    :type d: Int

    :rtype: bool
    :return: True if move valid, False if move invalid.
    """

    # Check if there are cards in the relevant pile. If so get the source card.
    if len(tableau[s]) >= 1:
        source_card = tableau[s][len(tableau[s]) - 1]

    # If list empty return False.
    if not tableau[s]:
        return False

    # If there are cards in the foundation pile get the destination card.
    if len(foundation[d]) >= 1:
        destination_card = foundation[d][len(foundation[d]) - 1]
    
    # If there is no destination card, check if the source card is an ace
    # and if it is return True, otherwise return False.
    elif not foundation[d]:
        if source_card.rank() == 1:
            return True
        else:
            return False

    # If the source card is one greater than the destination card in terms
    # of rank, then check if the suits are the same. Return True if both
    # statements are met. Otherwise return False.
    if source_card.rank() == (destination_card.rank() + 1):
        if source_card.suit() == destination_card.suit():
            return True
        else:
            return False
    else:
        return False
    
def move_tableau_to_foundation(tableau, foundation, s,d, undo_bool=False):
    """
    Moves a card from the tableau to the foundation as specified if valid. A 
    modification was made to the functions parameters. Undo_bool allows 
    the function to skip move validation if set as True. This allows the 
    program to execute normally illegal undo moves.

    :param tableau: The tableau list of lists.
    :type tableau: List of lists

    :param foundation: The foundation list of lists.
    :type foundation: List of lists.

    :param s: The tableau pile index.
    :type s: Int

    :param d: The foundation pile index.
    :type d: Int

    :rtype: bool
    :return: True if valid and move completed, false otherwise.
    """

    # Check validity of move and if valid pop the card and append it to the
    # correct pile. If undo bool set to true execute without validation for
    # move. Allows illegal undo moves.
    if valid_tableau_to_foundation(tableau, foundation, s, d) or undo_bool:
        source_card = tableau[s].pop()
        foundation[d].append(source_card)
        return True
    
    else:
        return False

def check_for_win(foundation):
    """
    Returns True if the game is won and False if not won.
    :param foundation: The foundation list of lists.
    :type foundation: List of lists
    :rtype: bool
    :return: True if won, otherwise False.
    """
    # Uses a list comprehension inside a conditional one line statement.
    # Checking if the number of cards inside the pile is 13 if so it appends 
    # 1 and if the length of the list is 4 i.e all foundations are filled 
    # return True otherwise return False.
    return True if (len([1 for foundation_pile in foundation if len(foundation_pile) == 13])) == 4 else False

def get_option():
    """
    Gets an option from the user. If the option is a card move it ensures
    the indicies are valid.

    :rtype: List, or None
    :return: A list of the option string and if the option is a move, the 
    indicies. If invalid input None is returned.
    """
    
    # Get input string, split each element into a list. Then strip each 
    # element of whitespace. Convert the first element to uppercase.
    input_option_str = input("\nInput an option (MTT,MTF,MFT,U,R,H,Q): ")
    input_option_list = input_option_str.split()
    input_option_list = \
    [input_option.strip() for input_option in input_option_list]
    input_option_list[0] = input_option_list[0].upper()

    if input_option_list[0] == 'MTT':
        # Convert the numbers into ints.
        input_option_list[1] = int(input_option_list[1])
        input_option_list[2] = int(input_option_list[2])

        # Check if the numbers are in valid range. If they are valid return the
        # list and if not return an Error message.
        if (7 >= input_option_list[1] >= 0) and \
        (7 >=input_option_list[2] >= 0):
            return input_option_list
        elif not(7 >= input_option_list[1] >= 0):
            print("Error in Source.")
            return None
        elif not(7 >=input_option_list[2] >= 0):
            print("Error in Destination")
            return None
    
    elif input_option_list[0] == 'MTF':
        # Convert the numbers into ints.
        input_option_list[1] = int(input_option_list[1])
        input_option_list[2] = int(input_option_list[2])

        # Check if the numbers are in valid range. If they are valid return the
        # list and if not return an Error message.
        if (7 >= input_option_list[1] >= 0) and (3 >=input_option_list[2] >= 0):
            return input_option_list
        elif not(7 >= input_option_list[1] >= 0):
            print("Error in Source.")
            return None
        elif not(3 >=input_option_list[2] >= 0):
            print("Error in Destination")
            return None
    
    elif input_option_list[0] == 'MFT':
        # Convert the numbers into ints.
        input_option_list[1] = int(input_option_list[1])
        input_option_list[2] = int(input_option_list[2])

        # Check if the numbers are in valid range. If they are valid return the
        # list and if not return an Error message.
        if (3 >= input_option_list[1] >= 0) and (7 >=input_option_list[2] >= 0):
            return input_option_list
        elif not(3 >= input_option_list[1] >= 0):
            print("Error in Source.")
            return None
        elif not(7 >=input_option_list[2] >= 0):
            print("Error in Destination")
            return None
    
    # Check the first element for validity.    
    elif input_option_list[0] == 'U':
        return input_option_list
    elif input_option_list[0] == 'R':
        return input_option_list
    elif input_option_list[0] == 'H':
        return input_option_list
    elif input_option_list[0] == 'Q':
        return input_option_list

    # If not valid give an error option.
    else:
        print("Error in option:")
        print(input_option_str)
        return None

def main():  
    print("\nWelcome to Streets and Alleys Solitaire.\n")
    option_list = ['C']   # Set to random value so that loop runs for first time.

    # If the option is Q quit the game.
    while option_list[0] != 'Q':

        # Start a new game and set the tableau and foundation.
        tableau, foundation = initialize()

        # Intialize an empty move_save_data list. List because the moves must
        # be in order.
        move_save_data = []
        display(tableau, foundation)
        print(MENU)

        # Runs the game, the statements break the loop when appropriate.
        while True:
            
            # Gets option w/ error checking loop.
            while True:
                option_list = get_option()
                if option_list != None:
                    break
            
            # Execute if a tableau to tableau move.
            if option_list[0] == 'MTT':
                # Try to make the move.
                move_bool = move_tableau_to_tableau(tableau, option_list[1], option_list[2])
                
                # If not valid give the error message.
                if not move_bool:
                    print("Error in move: {} , {} , {}".format(option_list[0], option_list[1], option_list[2]))
                    continue
                
                # If the game was won, print win message, display board, and start a new game.
                if check_for_win(foundation):
                    print("You won!\n")
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    break

                display(tableau, foundation)

                # Add the move the list of move_save_data.
                move_save_data.append(option_list)
            
            # Execute if a foundation to tableau move.
            elif option_list[0] == 'MFT':
                # Try to make the move.
                move_bool = move_foundation_to_tableau(tableau, foundation, option_list[1], option_list[2])
                
                # If not valid give the error message.
                if not move_bool:
                    print("Error in move: {} , {} , {}".format(option_list[0], option_list[1], option_list[2]))
                    continue

                # If the game was won, print win message, display board, and start a new game.
                if check_for_win(foundation):
                    print("You won!\n")
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    break

                display(tableau, foundation)

                # Add the move the list of move_save_data.
                move_save_data.append(option_list)

            # Execute if a tableau to foundation move.
            elif option_list[0] == 'MTF':
                # Try to make the move.
                move_bool = move_tableau_to_foundation(tableau, foundation, option_list[1], option_list[2])
                
                # If not valid give the error message.
                if not move_bool:
                    print("Error in move: {} , {} , {}".format(option_list[0], option_list[1], option_list[2]))
                    continue

                # If the game was won, print win message, display board, and start a new game.
                if check_for_win(foundation):
                    print("You won!\n")
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    break

                display(tableau, foundation)

                # Add the move the list of move_save_data.
                move_save_data.append(option_list)

            # If user wants to restart it breaks the loop and starts a new game.
            elif option_list[0] == 'R':
                break
            
            # Execute if user wants to undo move.
            elif option_list[0] == 'U':

                # If there are no valid moves made give an error message.
                if not move_save_data:
                    print("No moves to undo.")
                    
                # If there is a valid move to undo, execute.
                elif move_save_data:
                    # Pop the last move made.
                    save_data_list = move_save_data.pop()

                    # Execute a tableau to tableau move if the move to undo 
                    # was a tableau to tableau move. Reverse position of 
                    # destination and source. Set undo_bool to True so that if
                    # the move is illegal it can still execute.
                    if save_data_list[0] == 'MTT':
                        undo_move_bool = move_tableau_to_tableau(tableau, 
                        save_data_list[2], save_data_list[1], undo_bool=True)

                    # Execute a foundation to tableau move if the move to undo 
                    # was a tableau to foundation move. Reverse position of 
                    # destination and source. Set undo_bool to True so that if
                    # the move is illegal it can still execute.
                    elif save_data_list[0] == 'MTF':
                        undo_move_bool = move_foundation_to_tableau(tableau, 
                        foundation, save_data_list[2], save_data_list[1], 
                        undo_bool=True)

                    # Execute a tableau to foundation move if the move to undo 
                    # was a foundation to tableau move. Reverse position of 
                    # destination and source. Set undo_bool to True so that if
                    # the move is illegal it can still execute.
                    elif save_data_list[0] == 'MFT':
                        undo_move_bool = move_tableau_to_foundation(tableau, 
                        foundation, save_data_list[2], save_data_list[1], 
                        undo_bool=True)

                    print("Undo: {} {} {}".format(save_data_list[0], 
                    save_data_list[1], save_data_list[2]))
                    display(tableau, foundation)

            # Quit if Q is selected.
            elif option_list[0] == 'Q':
                break
            
            # Display menu if H selected.
            elif option_list[0] == 'H':
                print(MENU)

    print("Thank you for playing.")

if __name__ == '__main__':
     main()