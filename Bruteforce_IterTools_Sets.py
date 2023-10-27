"""
Refactored to use sets to allow for quicker derivation of the cannot_make list
"""

from itertools import product
coins = (1,2,5,10,20,50,100,200)

def main():
    max_value = max(coins)*3
    can_make = set()
    cannot_make = set()
    for coin_tuple in product(coins, repeat=3):
        can_make.add(sum(coin_tuple))

    cannot_make = set(range(max_value))
    cannot_make = cannot_make-can_make

    print("Possible")
    print(f"{sorted(can_make)}\n")
    print("Impossible")
    print(list(cannot_make))

if __name__ == "__main__":
    main()
