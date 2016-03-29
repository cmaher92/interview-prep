yesterdays_stock_prices = [10, 7, 5, 8, 11, 7]

def get_max_profit( yesterdays_stock_prices ):
    low_price = None
    high_price = None
    for price in yesterdays_stock_prices:
        if low_price == None or price < low_price:
            low_price = price
            # print low_price

    for price in yesterdays_stock_prices:
        if high_price == None or price > high_price:
            high_price = price
            # print high_price
            # 10, 11

    max_profit = high_price - low_price
    return max_profit

    # for price in yesterdays_stock_prices:
    #     if high_price == None or price > high_price:
    #         high_price = price
    #         max_profit = high_price - low_price

    # return max_profit
max_profit = get_max_profit( yesterdays_stock_prices )
print max_profit
