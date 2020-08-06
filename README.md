# make_class_bingo_cards
This script will create custom "bingo" cards for the specific purpose
to help students get to know each other.

The input to the script is a .csv file with category headings across the columns
The script it can handle as many category headings as needed.  Under each category
heading should be a list of "things" that fit under each heading.  There can be as many
as needed - each column doesn't need to be the same length

This script will make choose 25 random combinations of category headings and things under
the headings, and place them on a 5x5 bingo grid.  The idea is then that each student has to
connect 5 other students in a row by finding student who match the grid.

The script requires 2 command line inputs: (1) the .csv file name and (2a) the number of random 
bingo cards to make or (2b) the name of a plain text file with a list of labels to append to the output
file names.  For the second command line argument: if option 2a is used, then the output files will be 
that many bingo cards with filenames bingo_card_###.pdf; if option 2b is used, then the output files
will be equal to the number of labels in the given file with filenames bingo_card_LABEL.pdf

Note: because it is a .csv file, you cannot use commas in your file.  For example, I like to
use Hometown as a category but have to leave out the comma between city and state.
