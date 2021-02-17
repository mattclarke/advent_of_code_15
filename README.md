# advent_of_code_15
https://adventofcode.com/2015

## Day 1
### Part 1 & 2
* Looping and counting.

## Day 2
### Part 1 & 2
* Looping, sorting and counting.

## Day 3
### Part 1 & 2
* Looping and counting.

## Day 4
### Part 1 & 2
* Python's hashlib to the rescue. Being expected to implement our own hashing function seems unlikely for day 4.

## Day 5
### Part 1
* Using regex for parts of it for fun - can it be done in one regex...

No, but it is pipe-able! From the 'net: `cat input  | grep "[aeiou].*[aeiou].*[aeiou]" | grep "\(.\)\1" | egrep -v "(ab|cd|pq|xy)" | wc -l`
### Part 2
* I suck at regex, so just used brute force. The input strings are short enough that it runs quickly.

From the web, the first rule can be done with `re.search(r"(..).*\1", line)` and the second rule with `re.search(r"(.).\1", line)`

## Day 6
### Part 1
* Simple enough to do. Used regexes because day 5 showed me that I needed some practise!
### Part 2
* Slight variation.

Takes ~6 seconds to run each puzzle. Pypy takes < 1 second for both!

## Day 7
### Part 1
* Loop through the instructions solving and removing the ones that can be solved. Keep going until all are solved.
### Part 2
* Slight variation by changing the input for b to be the solution from part 1.

## Day 8
### Part 1
* Complete brain failure! Replace the "\" with "/" and suddenly everything becomes easier to reason about!
### Part 2
* First replace `\\` with `\\\\` and then `"` with `\\"` and it just drops out!

## Day 9
### Part 1
* Recursion to visit all the cities then find the minimum distance
### Part 2
* Easy - change from `min` to `max`!

## Day 10
### Part 1
* Read the string character by character and keep track of the current number and how many times it is seen.
### Part 2
* Repeat the calculation ten more times.

## Day 11
### Part 1
* Rules are simply enough to implement. Decided to "convert" the password to base-26 so it could be done with simple maths.
### Part 2
* Repeat the process one more time takes ~2 seconds.

## Day 12
### Part 1
* re.findall - don't forget the (possible) minus sign!
### Part 2
* Recurse through the structure and skip the "red" bits.

## Day 13
### Part 1
* Recursion to find the best arrangement, just track the happiness total.
### Part 2
* Modified to add "me" as None as the first person and clauses to ignore "me".

## Day 14
### Part 1
* Just looping for each second.
### Part 2
* Same, but track who has travelled furthest and give them a point.

## Day 15
### Part 1
* Recursion to try all the possible combinations - is there a better way? Takes ~3 seconds.
### Part 2
* Added an extra optional clause to check calories.

## Day 16
### Part 1
* Loop through the rules and remove any Sue that fails. That leaves us with one Sue.
### Part 2
* Use a customer comparator to take into account new rules - try to avoid stupid typos which result in the wrong result ;)

## Day 17
### Part 1
* First attempt using recursion is very slow (~25 seconds). As there are multiple containers the same size, I create a tuple
of the size and a unique number so they appear different when hashed, so I can use a set.
* TODO: can it be sped up?
### Part 2
* Keeping the solutions from part 1 made this trivial.

## Day 18
### Part 1
* Conway's game of life but with fixed bounds.
### Part 2
* Always ensure the corners are lit.

## Day 19
### Part 1
* Just need to remember that some molecules are more than one character, e.g. Si.
### Part 2
* This took an unholy amount of time (hours and hours!) - in the end I had to look on the web. The key insight was to
replace `Rn`, `Y` and `Ar` with `(`, `|` and `)` respectively then the target has the form of `ABC(DE)F(G|H)IJ` which
shows a structure to it. I then used regexes to reduce the target starting with the nested brackets and working outwards.
I think my solution can be simplified further, but I have had enough of it.

I included the one line solution I found on the web T.T

## Day 20
### Part 1
* Sieving works.
### Part 2
* Simple change

Originally tried a more complicated method which works but I don't fully understand it. Kept for future reference ;)

## Day 21
### Part 1
* Simple looping.
### Part 2
* Small change to track cost when losing.

## Day 22
### Part 1
* Took some time to get the game set up and to get the recursion working. Made a few mistakes with the limits.
### Part 2
* Should be simple right? Took hours to find subtle bug that only showed up in Part 2, see code comment.
Had to unwind the recursion to find it! Also resorted to trying a solution off thw web (without reading it) just to check
the puzzle wasn't broken - which of course it wasn't!

## Day 23
### Part 1
* Basic CPU with short instruction set. Didn't read the instructions properly and missed that jio is jump-if-one not
jump-if-odd. Wasted some time trying to work out what was wrong.
### Part 2
* Simple, just change the starting registers.

## Day 24
### Part 1
* Find combinations for the first compartment that add up to the target, then check it is possible to reach the target
from the remaining weights for the remaining compartments. Once there is a solution, even if it isn't the final one, we
can stop recursion on any paths which are worse, so that speeds it up.
### Part 2
* Added another compartment.

Using itertools to get the possible combinations makes this problem relatively trivial, but I didn't want to do that!

## Day 25
### Part 1 (the only part)
* Some basic maths to work out the maximum row number to hit the required row and column and then how to move through
them.
