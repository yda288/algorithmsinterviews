# algorithmsinterviews

I've seen a lot of recursive solutions for this but no DP ones (including the vowel constraint) so thought I would share mine:

Description:
============
Dynamic programming solution for counting the number of valid sequences of knights moves on the following keypad of a desired length subject to a maximum vowels constraint:

['A','B','C','D','E']
['F','G','H','I','J']
['K','L','M','N','O']
[' ', 1,  2,  3, ' ']

Defaulted to count sequences of digit length 17 with a max vowel constraint of 2.

Structure:
============

main.py - main entry point. Run this to print number of valid 17-key sequences on a single line to standard out.
tests.py - unittests for Keypad class designed to disable negative indexing or slicing so as to prevent consumers inadvertently wrapping around.
src/constants.py - constants used in program.
src/knightssequences.py - classes to model Keypad, Adjacency. 
src/solutions.py - dynamic programming based method to count the valid knights sequences on the keypad.

Performance:
============

Solution performance (excluding overhead to build Keypad and Adjacency graph):
 %timeit dp_count_sequences(keypad, adjacency, 17, 2)
1000 loops, best of 3: 1.2 ms per loop

Dependencies:
============
Python 3.5