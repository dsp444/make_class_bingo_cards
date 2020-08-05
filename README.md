# make_class_bingo_cards
This script will creat custom "bingo" cards for the specific purpose
to help students get to know each other.

The input to the script is a .csv file with category headings across the columns
The script it can handle as many category headings as needed.  Under each category
heading should be a list of "things" that fit under each heading.  There can be as many
as needed - each column doesn't need to be the same length

This script will make choose 25 random combinations of category headings and things under
the headings, and place them on a 5x5 bingo grid.  The idea is then that each student has to
connect 5 other students in a row by finding student who match the grid.

The script requires 2 command line inputs: 1) the .csv file name and 2) the number or random 
bingo cards to make.
Note: because it is a .csv file, you cannot use commas in your file.  For example, I like to
use Hometown as a category but have to leave out the comma between city and state.
