#!/usr/bin/python

import argparse

#         i
# [1050, 270, 1540, 3800, 2]
#                        j

# first pass profit = 270 - 1050 = -780
# second pass profit = 1540 - 270 = 1270


def find_max_profit(prices):
    max_profit_so_far = prices[1] - prices[0]

    # Loop through prices
    for prev in range(0, len(prices)):
        for current in range(prev + 1, len(prices)):
            current_profit = prices[current] - prices[prev]
            if current_profit > max_profit_so_far:
                max_profit_so_far = current_profit

    return max_profit_so_far


if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )

