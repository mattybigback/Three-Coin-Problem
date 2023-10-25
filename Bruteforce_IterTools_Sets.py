"""
Refactored to use sets.
This should make the result not in comparisons faster
"""

import itertools
coins = (1,2,5,10,20,50,100,200)
can_make = set()
cannot_make = set()

if __name__ == "__main__":
    for coin1, coin2, coin3 in itertools.product(coins, coins, coins):
        total=coin1+coin2+coin3
        if total not in can_make:
            can_make.add(total)

    for result in range(600):
        if result not in can_make:
            cannot_make.add(result)
    print("Possible")
    can_make=list(can_make)
    cannot_make=list(cannot_make)
    can_make.sort()
    print(f"{can_make}\n")
    print("Impossible")
    print(cannot_make)