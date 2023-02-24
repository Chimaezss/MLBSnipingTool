while True:
    # Required information for program
    test_price = input('What can you find the card for? ')
    buy_price = (int(test_price) * .90)
    print(f'Diamond Card: {buy_price - 500}.')
    print(f'Gold Card: {buy_price - 250}.')
    print(f'Silver Card: {buy_price - 100}.')
    # Here would be a prompt to quit, not displayed to reduce clutter
    if test_price == '-1': break