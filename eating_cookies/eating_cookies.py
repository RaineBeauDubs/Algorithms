#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement a solution that is more efficient than the naive recursive solution

# CM can eat 1, 2, or 3 (or 0) cookies at a time
# is given jar of 'n' cookies
# should return the number of way CM can eat the amount of cookies given to him in the jar
# ex.: `eating_cookies(3)` should return 4 (see README)

def eating_cookies(n, cache=None):
  # take in the given 'n'
  # tell this that it can eat 0, 1, 2, or 3 cookies at one time (okay, I seriously don't understand 0, though, because if we're counting zero, wouldn't each answer just be infinity? You can eat 0 cookies an infinite amout of times, or (personally) I think it shouldn't be counted at all, but it's specifically written. So that's it, then, I solved it, all answers to this question are "infinity.")
  # figure how many possible ways CM can consume any number of cookies represented by 'n'
  # prints that number of ways.
  pass

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')