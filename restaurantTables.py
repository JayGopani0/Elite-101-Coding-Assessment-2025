# ------------------------------------------------------------------------------------
# The following 2D lists mimic a restaurant seating layout, similar to a grid.
# 
# - Row 0 is a "header row":
#     - The first cell (index 0) is just a row label (0).
#     - The remaining cells are table labels with capacities in parentheses,
#       e.g., 'T1(2)' means "Table 1" has capacity 2.
#
# - Rows 1 through 6 each represent a distinct "timeslot" or "seating period":
#     - The first cell in each row (e.g., [1], [2], etc.) is that row's label (the timeslot number).
#     - Each subsequent cell shows whether the table (from the header row) is
#       free ('o') or occupied ('x') during that timeslot.
#
# In other words, restaurant_tables[row][column] tells you the status of a
# particular table (column) at a particular timeslot (row).
# ------------------------------------------------------------------------------------

# Shows the structure of the restaurant layout with all tables free ("o" = open).
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'o',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'o',      'o',      'o',      'o',      'o'],
    [3,        'o',      'o',      'o',      'o',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'o'],
    [5,        'o',      'o',      'o',      'o',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'o',      'o']
]

# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------

restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]


""" 
Level 1 - listing all tables that are currently free
We first have to traverse the 2d list by row to determine which timeslots are open for the specific table before
moving on to the next table. We then traverse by column to the next table before doing the same procedure. This should be done using 
a nested for loop to traverse both at the same time.
We also create a blank list to put all the information into it and return at the end of the code
"""
def free_tables(tables):  # taking the table parameter so that the code can work for any table
    free_tables = [] # list to hold information 
    for table_num in range(1, len(tables[0])):  # Iterate through columns (tables)
        statement = ""   # statement to append to list
        statement += ("Table " + str(tables[0][table_num]) + " at timeslot ")
        for timeslot in range(1, len(tables)):  # Iterate through rows (timeslots)
            if tables[timeslot][table_num] == "x":
                continue
            else:
               statement += (str(tables[timeslot][0]) + " ")
        free_tables.append(statement)
    return free_tables

# print(free_tables(restaurant_tables2))


"""
Level 2 - Party Size
We have to find a single table that can fit the part size. In order to do so, we should check the columns of tables that are greater
than or equal to the party size and then check the available time slots before returning the table. This needs a nested for loop like the 
previous level but with an embedded if statement to skip the tables that don't have the necessary capacity

"""



def party_size(tables):
    size = int(input("What is your party size? "))
    for table_num in range(1, len(tables[0])):  # Iterate through columns (tables)
        table_size = int((tables[0][table_num])[3]) # Finds the capacity of the table by getting the 4th character and making it an integer
        if table_size < size: # to determine if the table can hold the amount of guests
            continue # moves to the next table if it cannot
        else: 
            for timeslot in range(1, len(tables)):  # Iterate through rows (timeslots)
                if tables[timeslot][table_num] == "o":
                    return "Table " + str(tables[0][table_num]) + " is avaiable at timeslot " + str(tables[timeslot][0])


# print(party_size(restaurant_tables2))


"""
Level 3 - Party size AND all are free
Also similar to the previous levels, this will find which tables are free and fit the capacity, not just returning the first table it finds.
Similar code to the level 2 program will be used with changes to how the information is stored.

"""

def all_party_size(tables):
    all_free_tables = [] # Used to store all info
    size = int(input("What is your party size? "))
    for table_num in range(1, len(tables[0])):  # Iterate through columns (tables)
        table_size = int((tables[0][table_num])[3]) # Finds the capacity of the table by getting the 4th character and making it an integer
        if table_size < size: # to determine if the table can hold the amount of guests
            continue # moves to the next table if it cannot
        else: 
            for timeslot in range(1, len(tables)):  # Iterate through rows (timeslots)
                if tables[timeslot][table_num] == "o": 
                    all_free_tables.append("Table " + str(tables[0][table_num]) + " is avaiable at timeslot " + str(tables[timeslot][0])) # adds to the list to later be returned
    return all_free_tables

# print(all_party_size(restaurant_tables2))



"""
Level 4 - Adjacent Seats

"""

def adjacency(tables):
    adjacency_combos = [] # Used to store all info
    size = int(input("What is your party size? "))
    for table_num in range(1, len(tables[0])):  # Iterate through columns (tables)
        table_size = int((tables[0][table_num])[3]) # Finds the capacity of the table by getting the 4th character and making it an integer
        if table_size < size: # to determine if the table can hold the amount of guests
            for timeslot in range(1, len(tables)):  # Iterate through rows (timeslots)
                if tables[timeslot][table_num] == "o": 
                    if tables[timeslot][table_num+1] == "o":
                        table_size += int((tables[0][table_num+1])[3])
                        if table_size >= size:
                            adjacency_combos.append((str(tables[0][table_num]) + " and " +  str(tables[0][table_num+1]) + " can fit the party"))
                    
        else: 
            continue
            
    return adjacency_combos

print(adjacency(restaurant_tables2))