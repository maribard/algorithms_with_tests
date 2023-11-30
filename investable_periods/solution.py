


def find_investable_periods(price, max_price, min_price):
    periods = []
    for elem_h in range(len(price) - 1):
        head = [price[elem_h]]
        for elem_t in range(elem_h + 1, len(price) + 1):
            tail = price[elem_h + 1:elem_t]
            possible_periods = head + tail
            if max(possible_periods) == max_price and min(possible_periods) == min_price:
                periods.append(possible_periods)

    return len(periods)



print(find_investable_periods([1, 2, 3, 2], 3, 2))
