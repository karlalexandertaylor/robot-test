#####################################
# Version 1.1 of Distance Calculator
#
# Purpose = Work out distance travelled from initial start point.  Distance is calculated based on how the crow flies between the two points
# The programme also outputs the number actual forward movements
#
#####################################

# Imported modules
import math
import sys
import os.path

# Variables
debug_check = ''
DEBUG = 0
R = 0  # Number of right movements
L = 0  # Number of left movements
F = 0  # Number of forward movements
X = 0  # Distance horizintally
Y = 0  # Distance vertically
facing = 'N'  # Direction facing - values N, E, S, W
distance = 0  # Distance travelled
line_value = ''
size_side_1 = 0
size_side_2 = 0
size_side_3 = 0
size_side_4 = 0
current_side = 1
store_last_facing = 'N'

# Function to check arguments


def check_arguments():
    global debug_check
    global DEBUG

    # Check number of arguments
    if len(sys.argv) > 3:
        argument_exit()
    if len(sys.argv) < 2:
        argument_exit()

    # Validate the file argument is a file
    result = os.path.isfile(sys.argv[1])
    if result == False:
        print ('Invalid File')
        exit()

    # Check the debug setting
    if len(sys.argv) == 3:
        debug_check = sys.argv[2]
    if debug_check == '1':
        DEBUG = 1
    elif debug_check == '0':
        DEBUG = 0
    elif debug_check == '':
        DEBUG = 0
    else:
        argument_exit()


def argument_exit():
    print ('Invalid argument For debug - usage is -> python omingen_prog1.py filename debug -> where filename is the input file and debug is either 1 for on or 0 for off')
    exit()

# Function to evaluate file line


def evaluate_line():
    if (DEBUG == 1):
        debug_function('evaluate_file_line')
    if (line_value == 'F'):
        move_function()
    elif (line_value == 'R' or line_value == 'L'):
        facing_function(line_value)
    else:
        print ('Invalid line character - ignoring')

# Function to handle movement


def move_function():
    global X
    global Y
    global F
    global facing
    global store_last_facing
    global current_side
    global size_side_1
    global size_side_2
    global size_side_3
    global size_side_4

    # Update the coords
    if (facing == 'N'):
        Y = Y + 1
    elif (facing == 'E'):
        X = X + 1
    elif (facing == 'S'):
        Y = Y - 1
    else:
        X = X - 1

    # Update the number of movements
    F = F + 1

    # Check to see if direction has moved from previous direction
    # If different start calculating the next side
    if (store_last_facing != facing):
        if (current_side < 4):
            current_side = current_side + 1
            store_last_facing = facing

    # Calculate size of side
    if (current_side == 1):
        size_side_1 = size_side_1 + 1
    elif (current_side == 2):
        size_side_2 = size_side_2 + 1
    elif (current_side == 3):
        size_side_3 = size_side_3 + 1
    else:
        size_side_4 = size_side_4 + 1

    if (DEBUG == 1):
        debug_function('square_sides')

# Function to work out the way you are facing


def facing_function(direction):
    global facing
    if (direction == 'R'):
        if (facing == 'N'):
            facing = 'E'
        elif (facing == 'E'):
            facing = 'S'
        elif (facing == 'S'):
            facing = 'W'
        else:
            facing = 'N'
    else:
        if (facing == 'N'):
            facing = 'W'
        elif (facing == 'W'):
            facing = 'S'
        elif (facing == 'S'):
            facing = 'E'
        else:
            facing = 'N'
    if (DEBUG == 1):
        debug_function('facing_function')


def debug_function(debug_command):
    # Debug function to share values to help identify issues
    if (debug_command == 'coords'):
        print ('*****DEBUG OUTPUT -  final position *****')
        print ('Horizontal coordinate = ' + str(X))
        print ('Vertical coordinate = ' + str(Y))
        print ('*****')
    elif (debug_command == 'evaluate_file_line'):
        print ('*****DEBUG OUTPUT -  evaluate line *****')
        print ('File line = ' + line_value)
        print ('Current direction faced = ' + facing)
        print ('*****')
    elif (debug_command == 'facing_function'):
        print ('*****DEBUG OUTPUT - facing function *****')
        print ('Direction of turn = ' + line_value)
        print ('New location faced = ' + facing)
        print ('*****')
    elif (debug_command == 'square_sides'):
        print (size_side_1)
        print (size_side_2)
        print (size_side_3)
        print (size_side_4)
        print ('X=' + str(X) + 'Y=' + str(Y) + 'facing=' +
               facing + 'lastfacing=' + store_last_facing)
        print (current_side)
    else:
        print ('*****')
        print ('Unknown error')
        print ('*****')

# Main code function
# Line file read loop


check_arguments()

# Get file name to evaluate - note argument 0 is the python code file and argument 1 is the file to be analysed
filepath = sys.argv[1]

# Calculate if final position is the same as the start position
with open(filepath) as fp:
    line = fp.readline()
    line_value = line.strip()
    evaluate_line()
    cnt = 1
    while line:
        line = fp.readline()
        line_value = line.strip()
        if (line_value == 'F' or line_value == 'R' or line_value == 'L'):
            evaluate_line()
        cnt += 1

fp.close()

if (DEBUG == 1):
    debug_function('coords')

if (X != 0 and Y != 0):
    print ('Does not return to start position')
    exit()

if (size_side_1 == size_side_2 == size_side_3 == size_side_4):
    print ('It is a circle')
else:
    print ('Not a circle')
