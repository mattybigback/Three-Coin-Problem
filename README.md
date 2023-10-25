# The Three Coin Problem

Experiments on solving the three coin problem.

## What is the three coin problem?

Imagine you have a big bag of different types of coins. If you reach in and pull out three coins, what values could the three coins add up to?

For example, with the standard set of British coins (1p, 2p, 5p, 10p, 20p, 50p, £1 and £2), how many different combinations can you make using three coins?

## About the solutions

All solutions print a list of possible values followed by impossible values, both in ascending order.

The first three solutions are based around a naive bruteforce of the list of coins. Itertools is introduced to make the code more concise, and sets are introduced to speed up matching.

## Benchmark

I have included a small bash script that benchmarks each solution using python's timeit module. The results below were run on a laptop with an i7 7500U running at 3.5 GHz. Note that outputing the scripts to the standard console will slow them down considerably as console outputs are much slower than writing to a file.

#### Bruteforce_NestedFor.py
100 loops, best of 5: 34 msec per loop

#### Bruteforce_IterTools.py
100 loops, best of 5: 1.06 msec per loop

#### Bruteforce_IterTools_Sets.py
100 loops, best of 5: 209 usec per loop

There were considerable gains to be made by using itertools and sets - a speed increase of over 500%!

