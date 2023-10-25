"""
Basic bruteforce solution using nested for loops.
Just look at that indentation!
"""

coins = (1,2,5,10,20,50,100,200)

def main():
    can_make = []
    cannot_make = []
    for coin1 in coins:
        for coin2 in coins:
            for coin3 in coins:
                total = coin1+coin2+coin3
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

if __name__ == "__main__":
    main()
