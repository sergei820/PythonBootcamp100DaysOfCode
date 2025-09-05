
def find_highest_bidder(bidding_dict: dict):
    winner = ''
    max_bid = 0
    for key in bidding_dict:
        bid_amount = bidding_dict[key]
        if bid_amount > max_bid:
            winner = key
            max_bid = bidding_dict[key]
    print(f"The winner is {winner} with a bid of ${bidders[winner]}")

should_continue = True
bidders = {}

while should_continue:
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    bidders[user_name] = user_bid

    proceed = input("Are there any other bidders? Type y/n\n")
    if proceed == "y":
        should_continue = True
        print("\n" * 10)
    else:
        should_continue = False
        find_highest_bidder(bidders)
