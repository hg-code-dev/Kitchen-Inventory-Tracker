# Initial kitchen stock variables
available_eggs = 1
available_flour = 2
available_sugar = 3

def check_kitchen_stock():
    """
    Prints a summary of all available kitchen items.
    """
    # Calculate total number of items
    total_items = available_eggs + available_flour + available_sugar
    
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

# Show initial stock
check_kitchen_stock()

def use_eggs(available_eggs, eggs_to_use):
    """
    Attempts to use a given number of eggs.
    Returns the updated number of eggs after use.
    """
    # Check if there are enough eggs to use
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

    # Use the eggs and report the action
    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

# Use 1 egg and print the original variable (note: this does NOT update available_eggs)
use_eggs(available_eggs, 1)
print(available_eggs)  # Still 1 because the returned value wasn't assigned

def make_fried_egg(available_eggs):
    """
    Tries to make a fried egg.
    Uses 1 egg if available and returns the updated egg count.
    """
    # Check if at least one egg is available
    has_enough_eggs = available_eggs >= 1

    if has_enough_eggs:
        # Use one egg and update the count
        available_eggs = use_eggs(available_eggs, 1)
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')

    return available_eggs

# Make a fried egg and update the global egg count
available_eggs = make_fried_egg(available_eggs)

# Show updated stock
check_kitchen_stock()
