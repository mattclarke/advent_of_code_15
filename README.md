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
