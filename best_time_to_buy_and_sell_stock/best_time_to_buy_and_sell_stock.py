def max_profit(prices):
    max_profit = 0
    left = 0
    right = 1
    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right]-prices[left]
            if profit > max_profit:
                max_profit = profit
        else:
            left = right
        right += 1
    return max_profit