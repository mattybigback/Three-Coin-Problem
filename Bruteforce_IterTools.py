"""
Refactored to use itertools.
Why use three loops when you can hide them with syntactic sugar?
"""

import itertools
coins = (1,2,5,10,20,50,100,200)
can_make = []
cannot_make = []

if __name__ == "__main__":
    for coin1, coin2, coin3 in itertools.product(coins, coins, coins):
        total=coin1+coin2+coin3
        if total not in can_make:
            can_make.append(total)

    for result in range(600):
        if result not in can_make:
            cannot_make.append(result)
    can_make.sort()
    print("Possible")
    print(f"{can_make}\n")
    print("Impossible")
    print(cannot_make)