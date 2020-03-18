#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # Find maximum profit
  # Loop through prices keep track of the largest number
  # Each iteration subtract the current price from the largest number
  # if the result is larger than the current max profit then update
  # return max profit after loop
  largest_stock = prices[0]
  smallest = prices[0]
  max_profit =  prices[1] - smallest
  print(max_profit)
  for i in prices[1:]:
    print(i)
    if i - smallest > max_profit:
      max_profit = i - smallest
    if i < smallest:
      smallest = i
    print(F"smallest {smallest} maxproft {max_profit}")
  return max_profit
# find_max_profit([100, 90, 80, 50, 20, 10])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))