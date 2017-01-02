from .constants import CONST_VOWELS

def dp_count_sequences(keypad, graph, digit_length, max_vowels_constraint):
    """Returns the sum of digit sequences ending in each keypad letter. 
     
     DP state for ith iteration:
     
      A, B, C, D, E, F, G, H, I ... 1, 2, 3
     [                                     ] count digit seq ending in each letter with 0 max vowels
     [                                     ] ... with 1 max vowels
     [                                     ] ... with 2 max vowels
     
    Keyword arguments:
    keypad -- Keypad representation
    graph -- Adjacency graph
    digit_length -- desired digit sequence length
    max_vowels_constraint -- maximum permissible vowels in each digit sequence
    """
    
    flat_keypad = keypad.flatten()
    key_to_idx = keypad.key_to_idx()

    ith_state = [[
                     0 if _ in CONST_VOWELS else 1 for _ in flat_keypad
                     ]] ##count of digit sequences with maximum of 0 vowels
                     
    ith_state.extend([ 
                     len(flat_keypad)*[1] for _ in range(max_vowels_constraint)
                     ]) ##count of digit sequences with maximum of 1, 2 ... n 
                        ##max_vowel_constraint vowels. Final row is of interest.

   
    for i in range(1,digit_length):
        tail = ith_state ##persist this state for future iterations
        ith_state = [
                        len(flat_keypad)*[0] for _ in range(max_vowels_constraint + 1)
                        ] 
		## IMPORTANT: DO NOT rephrase this as e.g. 3*[[0]*18] 
		## https://docs.python.org/3/faq/programming.html#faq-multidimensional-list
                        
        for source,destinations in graph.items():
            idx_src = key_to_idx[source]
            for c in range(len(ith_state)):
                if source not in CONST_VOWELS or c > 0:
                    vowel_adjusted_lookup = (c-1 if source in CONST_VOWELS else c) ##offset the lookup depth if the current is a vowel
                    for dest in destinations:
                        idx_dest = key_to_idx[dest]
                        ith_state[c][idx_src] += tail[vowel_adjusted_lookup][idx_dest]
                   
    return sum(ith_state[max_vowels_constraint])