#!/usr/bin/python

import sys



def rock_paper_scissors(n):
  def helper_func(n, arr):
    newarr = []
    outcomes = ['rock', 'paper', 'scissors']
    print("Inside helper: ", n, arr)

    # print("Look here: ", [n*[x] for x in outcomes])
    # if n == 1:

    if n == 0:
      return [[]]
    elif len(arr) == 3**n:
      return 0

    # for x in arr:
    #     newarr.append([x] * helper_func(n, outcomes))
    return [[x] for x in outcomes]



    # return [helper_func([x], arr) for x in outcomes]

  # master_list.append(helper_func(n, master_list))
  return [x*n for x in helper_func(n, [])]



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
