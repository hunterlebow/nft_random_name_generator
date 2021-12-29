# Name Generator for an NFT Project
Author: Hunter Lebow

## Formula 
Adjective + Animal + Club Type + Club (i.e. Bored Ape Yacht Club)

In 'rng.py' a hyperparameter to the name generation is k.  An efficient and optimized k value should not be be greater than the length of the largest text file in order to minimize repeats.  'rng.py' uses random.choices(list, k) which does allow for repeats, which is neccessary for the context of this name generator.  Read more about the entire random library and random.choices() on StackOverFlow or other online resources.

## Output
All randomly generated NFT project names are written to output.csv.
In output.csv in this repository, there are example generated names when k = 20, adjustable in rng.py.


## Forks & Citations:
adjective text file: https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913

animals text file: https://gist.github.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54

club type text file created by Hunter Lebow. 

Feel free to add or subtract from any of the text files. Thanks.
