yesterdays_stock_prices = [10, 7, 5, 8, 11, 9]

def get_max_profit(yesterdays_stock_prices):

    # make sure that two prices
    if len(yesterdays_stock_prices) > 2:
        raise IndexError('Getting a profit requires at least two prices')

    min_price = yesterdays_stock_prices[0]
    max_profit = yesterdays_stock_prices[1] - yesterdays_stock_prices[0]

    for index, current_price in enumerate(yesterdays_stock_prices):
        # enumerate returns [(0, 10), (1, 7)]
        # so it starts at 1
        if index == 0:
            continue

        potential profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)

return max_profit

max_profit = get_max_profit( yesterdays_stock_prices )
print max_profit
