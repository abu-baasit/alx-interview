#!/usr/bin/python3
"""Changes from within"""
   
   
def make_change(coins, total):
    """Determines the fewest number of coins needed
         to meet a given amount total"""
    if total <= 0:
        return 0
          
    total_coins = 0
    coins_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total - total_coins) // coin
        total_coins += r * coin
        coins_used += r
        if total_coins == total:
            return coins_used
    return -1
