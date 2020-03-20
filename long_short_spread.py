"""
long_short_spread.py
Nicholas Noboa
Created 3/20/20
"""


def main():
    user_input = input("List or Calculate: ")
    if user_input.upper() == "LIST":
        list_spread()
    elif user_input.upper() == "CALCULATE":
        calculator()


def list_spread():
    tqqq_relative_price = input("TQQQ Price: ")
    sqqq_relative_price = input("SQQQ Price: ")
    into_each = input("Spread Amount: ")
    tqqq_price = float(tqqq_relative_price) - 1  # Drop by $1.00 to create +/-
    sqqq_price = float(sqqq_relative_price) - 1  # effect below.
    spread = float(into_each)

    tqqq_spread = {}
    sqqq_spread = {}

    for i in range(0, 201):  # +/- $1.00
        buying_tqqq = spread / tqqq_price
        tqqq_spread[round(tqqq_price, 2)] = round(buying_tqqq, 0)
        tqqq_price = tqqq_price + 0.01

    for i in range(0, 201):
        buying_sqqq = spread / sqqq_price
        sqqq_spread[round(sqqq_price, 2)] = round(buying_sqqq, 0)
        sqqq_price = sqqq_price + 0.01

    print("TQQQ (Price | Quantity)")
    for price in tqqq_spread:
        print(price, tqqq_spread[price])

    print("")
    print("SQQQ (Price | Quantity)")
    for price in sqqq_spread:
        print(price, sqqq_spread[price])


def calculator():
    run = True
    while run is True:
        relative_price = input("Price: ")
        into_each = input("Spread Amount: ")
        price = float(relative_price)
        spread = float(into_each)
        to_buy = spread / price
        print(round(to_buy, 0))
        more_calc = input("Quit (Y|N) ")
        if more_calc.upper() == "Y":
            run = False


main()
