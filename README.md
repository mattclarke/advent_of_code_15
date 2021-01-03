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
