# Import Libraries
import json
import math
import sys
import boto3

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

def lambda_handler(event, context):

    # Function to evaluate file line
    def evaluate_line():
        if (line_value == 'F'):
            move_function()
        elif (line_value == 'R' or line_value == 'L'):
            facing_function(line_value)
        else:
            print('Invalid line character - ignoring')

    # Function to handle movement
    def move_function():
        global X
        global Y
        global F
        global facing
        if (facing == 'N'):
            Y = Y + 1
        elif (facing == 'E'):
            X = X + 1
        elif (facing == 'S'):
            Y = Y - 1
        else:
            X = X - 1
        F = F + 1

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

    def handle_negative_coord():
        # Handle negative coordinates if south or west of start point
        global X
        global Y
        if X < 0:
            X = X * -1
        if Y < 0:
            Y = Y * -1

    def calculate_distance_from_centre():
        # Forumla to work out distance - pythogarus theorem -> c(squared) = a(squared) + b(squared)
        global distance
        distance = (X ** 2) + (Y ** 2)
        distance = round(math.sqrt(distance), 3)

    # Main code function
    # Line file read loop

    # Get file name to evaluate - note argument 0 is the python code file and argument 1 is the file to be analysed
    s3 = boto3.client('s3')

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    obj = s3.get_object(Bucket=bucket, Key=key)

    for line in obj['Body'].read().decode('utf-8').splitlines():
        line_value = line.strip()
        evaluate_line()

    # Fix negative coords
    handle_negative_coord()

    # Calculate distance
    calculate_distance_from_centre()

    # Print output
    print('Final position is ' + str(X) +
      ' horizontal and ' + str(Y) + ' vertical')
    print('Your distance from the start point is ' + str(distance))
    print('You have moved ' + str(F) + ' spaces')

    # TODO implement
    return {
        'statusCode': 200
    }
    
