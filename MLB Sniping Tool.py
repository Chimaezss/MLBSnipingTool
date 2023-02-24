card_list = []

while True:
    # Required information for program
    test_price = input('What can you find the card for? ') # Here would be a prompt to quit, not displayed to reduce clutter
    if test_price == '-1': break
    elif test_price == '-2': # Prompt for player info would be here, not present for less clutter
        player_info = input('Enter player information: ')
        card_list.append(player_info)
    elif test_price == '-3':
        print(card_list)
    else:
        buy_price = (int(test_price) * .90)
        print(f'Silver Card: {buy_price - 100}.')
        print(f'Gold Card: {buy_price - 250}.')
        print(f'Diamond Card: {buy_price - 500}.')