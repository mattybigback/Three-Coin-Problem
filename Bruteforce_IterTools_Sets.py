"""
Refactored to use sets.
This should make the result not in comparisons faster
"""

import itertools
coins = (1,2,5,10,20,50,100,200)

def main():
    max_value = max(coins)*3
    can_make = set()
    cannot_make = set()
    for coin1, coin2, coin3 in itertools.product(coins, coins, coins):
        total=coin1+coin2+coin3
        if total not in can_make:
            can_make.add(total)

    for result in range(max_value):
        if result not in can_make:
            cannot_make.add(result)
    print("Possible")
    can_make=list(can_make)
    cannot_make=list(cannot_make)
    can_make.sort()
    print(f"{can_make}\n")
    print("Impossible")
    print(cannot_make)

if __name__ == "__main__":
    main()
