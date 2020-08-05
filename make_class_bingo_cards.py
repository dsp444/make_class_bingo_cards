#######################
# This script will creat custom "bingo" cards for the specific purpose
# to help students get to know each other.
#
# The input to the script is a .csv file with category headings across the columns
# The script it can handle as many category headings as needed.  Under each category
# heading should be a list of "things" that fit under each heading.  There can be as many
# as needed - each column doesn't need to be the same length
#
# This script will make choose 25 random combinations of category headings and things under
# the headings, and place them on a 5x5 bingo grid.  The idea is then that each student has to
# connect 5 other students in a row by finding student who match the grid.
#
# The script requires 2 command line inputs: 1) the .csv file name and 2) the number or random 
# bingo cards to make.
# Note: because it is a .csv file, you cannot use commas in your file.  For example, I like to
# use Hometown as a category but have to leave out the comma between city and state.
#
# Version 1.0    Dan Puperi    8/05/2020
#
#######################

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import sys, random, os

OUT=sys.stdout.write

# Define the grid size (square is only option)
BINGO_SIZE = 5

# How big is the card in inches (it is square)
PHYSICAL_SIZE = 8   

#######################
# Read in all data from the input file and return it as a list of entries (pseudo-dictionary like)
# I kind of hate myself for not using a dictionary, but it is too easy to grab a random sample from a list
def read_input_file( fname ):
    output_list = []
    with open( fname ) as file:
        lines = file.readlines()
    headings = lines[0].strip().split(',')
    for line in lines[1:]:
        pieces = line.strip().split(',')
        i = 0
        for piece in pieces:
            if piece.strip() != '':
                output_list.append( '%s:%s' % (headings[i].strip(),piece.strip()) )
            i = i + 1
    return output_list
#######################

#######################
# Use matplotlib to make a graphical bingo card and save it to a .pdf file
def make_bingo_card( output_fname, squares ):
    fig = plt.figure()
    fig.set_size_inches( PHYSICAL_SIZE,PHYSICAL_SIZE )
    ax1 = fig.subplots( 1,1 )

#    Create the background grid and make it look pretty
    ax1.set_xticks( np.arange(BINGO_SIZE+1) )
    ax1.set_yticks( np.arange(BINGO_SIZE+1) )
    ax1.set_xticklabels( [] )
    ax1.set_yticklabels( [] )
    ax1.tick_params( axis="both", which="both",length=0 )
    ax1.grid( True )
  
#    Put text into each square  
    for i in range( 0,BINGO_SIZE ):
        for j in range( 0,BINGO_SIZE ):
            label1=squares[j+i*5].split(':')[0]
            label2=squares[j+i*5].split(':')[1]
            ax1.text( i+0.5,j+0.85,label1,ha="center",va="center", fontsize=choose_font_size( label1 ), fontweight='bold' )
            ax1.text( i+0.5,j+0.7,label2,ha="center",va="center", fontsize=choose_font_size( label2 ) )

#    Save the card to a .pdf file
    pp = PdfPages( output_fname )
    pp.savefig( plt.gcf() )
    pp.close()
#######################

#######################
# This function returns the font size that should be used for the test to fit properly in a square
# It depends on the length of the text and was found by a bit of trial and error for a 5x5
# bingo card that was 8" x 8" big
def choose_font_size( text ):
    if len(text) <= 13:
        return 10
    if len(text) <= 16:
        return 9
    if len(text) <= 19:
        return 8
    if len(text) <= 22:
        return 7
    if len(text) <= 25:
        return 6
    return 5
#######################

#######################
# Function to write usage information to the command line.  Helps user if they provide bad input
def usage():
    OUT( '\nClass bingo card maker\n\n' )
    OUT( ' usage: make_class_bingo_cards.py input_file_name number_of_unique_cards\n\n' )
    OUT( '    The input file name must be a .csv file with columns for each category and contains\n' )
    OUT( '    rows that list things that belong with each categoty.\n' ) 
    OUT( '    The number_of_unique_cards must be an integer and tells the script how many bingo cards\n' )
    OUT( '    to make.  The output files will be named bingo_card_XXX.pdf\n\n' )
#######################

#######################
# Entry point into the program.
if __name__ == '__main__':

# If there aren't exactly 2 command line arguments (input_file_name and number of cards to make), then 
# display the instructions of how to use this program.
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

# Get command line imputs and do some error checking
    input_fname = sys.argv[1]
    if not os.path.exists( input_fname ):
        OUT( '\nERROR: could not find your input file name.\n\n' )
        usage()
        sys.exit(1)
    try:
        num_cards = int( sys.argv[2] )
    except:
        OUT( '\nERROR: count not interpret how many bingo cards to make.  The 2nd input must be an integer.\n\n' )
        usage()
        sys.exit(1)

# Read in the input file - this will return a list of everything in the input file
    input_data = read_input_file( input_fname )

# Create the requested number of bingo cards by looping through the list and choosing a random sample for each one
    for i in range( 1,num_cards+1 ):
        try:
            this_card = random.sample( input_data, BINGO_SIZE*BINGO_SIZE )
        except:
            OUT( '\nERROR: did not have enough data in input file to grab %d random inputs\n\n' % (BINGO_SIZE*BINGO_SIZE) )
            sys.exit(1)

#     Now make the bingo card
        make_bingo_card( "bingo_card_%03d.pdf"%i, this_card )
#
#######################
