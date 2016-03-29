yesterdays_stock_prices = [10, 7, 5, 8, 11, 9]

def get_max_profit( yesterdays_stock_prices ):
    low_price = None
    high_price = None
    max_profit = 0

    for price in yesterdays_stock_prices:
        if low_price == None or price < low_price:
            low_price = price
        elif high_price == None or price > high_price:
            high_price = price

    try:
        max_profit = high_price - low_price
    except TypeError:
        max_profit = 0
        return max_profit
    else:
        return max_profit

    # return max_profit
max_profit = get_max_profit( yesterdays_stock_prices )
print max_profit
