from src.knightssequences import Keypad, Adjacency
from src.solutions import dp_count_sequences

if __name__ == "__main__":
	
	keypad = Keypad([
    ['A','B','C','D','E'],
    ['F','G','H','I','J'],
    ['K','L','M','N','O'],
    [' ', 1,  2,  3, ' ']
    ])
	
	adjacency = Adjacency(keypad).build_adjacency()
	
	soln = dp_count_sequences(keypad, adjacency, 17, 2)
	
	print(soln)
	
	
	