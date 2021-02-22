# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title: Flip Coin

import random

def flipCoin():
    heads = 0 # track heads amount
    tails = 0 # track tails amount
    headspercent = 0 # heads percentage
    tailspercent = 0 # tails percentage

    for i in range(1000): # run the experiment 1000 times
      coin=random.randint(1,2) # assign a value to coin, either 1 or 2

      if coin==1: # if coin value is assigned as 1
          heads+=1 # increase heads count by 1
      # else: # if coin value is assigned something other than 1
       #   tails+=1 # increase tails count by 1

    headspercent = heads / 10.0 # since we're rolling 1000 times, /10 will give percentage
    tailspercent = 100.0 - headspercent # no need to recalculate 100 - heads = tails %

    print("Heads percent: " + str(headspercent)) # printing the values on screen
    print("Tails percent: " + str(tailspercent)) # converting numbers to string by str()

flipCoin() # calling the function
