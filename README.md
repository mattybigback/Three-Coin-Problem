# The Three Coin Problem

Experiments on solving the three coin problem.

## What is the three coin problem?

Imagine you have a big bag of different types of coins. If you reach in and pull out three coins, what values could the three coins add up to?

For example, with the standard set of British coins (1p, 2p, 5p, 10p, 20p, 50p, £1 and £2), how many different combinations can you make using three coins?

## About the solutions

All solutions print a list of possible values followed by impossible values, both in ascending order.

The first three solutions are based around a naive bruteforce of the list of coins. Itertools is introduced to make the code more concise, and sets are introduced to speed up matching.