# This program tracks the purchases for a gift card worth $200.
# The user can purchase at most 5 items with the gift card.


def main():
    card_balance = 200   # Initial amount of the gift card
    items_purchased = 0  # Initial number of item purchased
    # The outer loop: as long as the card still have a balance and the user has not purchased more than 5 items
    while card_balance > 0 and items_purchased < 5:
        print('')
        print('You can purchase up to ', 5 - items_purchased, ' items with $', card_balance)
        price=input('  Enter item price: ')
        # The inner loop handles the input validation: prompt the user for the item price,
        # and if it is not valid, continue to prompt until a valid value is provided
        while (not price.isnumeric()):
            print('Price must be an integer number')
            price=input('  Enter a correct item price: ')
        # Once a valid price is provided, update the card_balance and items_purchased
        price=int(price)
        card_balance=card_balance-price
        items_purchased = items_purchased + 1
        # if the item costs too much, display a message and do inverse operation to eliminate the effects of errors
        if card_balance<0:
            print('That item costs too much! ')
            card_balance=card_balance+price
            items_purchased = items_purchased - 1
    # Call display_summary to display the final number of items purchased and amount of gift card spent
    display_summary(items_purchased, card_balance)


# This function displays a final message that summarizes the number of items purchased
# and the amount spent from the gift card.
# The function must include and use the 2 arguments: items_purchased and card_balance
def display_summary(items_purchased, card_balance):
    # Print the summary here
    print('')
    print('You purchased ', items_purchased, ' items totaling $', 200 - card_balance)

main()


