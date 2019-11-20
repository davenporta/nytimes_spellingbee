import sys
from tqdm import tqdm

puzzle = sys.argv[1].lower()
center = puzzle[0]
puzzle_set = set(puzzle)

if (len(puzzle) == 7):
    puzzle_str = """ %s  %s\n
    %s  %s  %s\n
     %s  %s\n
    """ % (puzzle[1], puzzle[2], puzzle[3], center, puzzle[4], puzzle[5], puzzle[6])
    print("Entered Puzzle:")
    print(puzzle_str)
    print("Solving... \n")

    with open('processed.txt') as f:
        words = f.read().splitlines()

    solutions = []

    for w in tqdm(words):
    	wset = set(w)
    	if (center in wset) and wset <= puzzle_set:
    		if len(wset) == 7:
    			w += " (Panagram!)"
    		solutions.append(w)

    solutions.sort()

    #print()
    #print(solutions)
    print()
    for w in solutions:
    	print(w)
else:
    print("ERROR: Invalid Size")
