# TODO-1: Ask the user for input
print("Welcome to bidding aution !")


# TODO-4: Compare bids in dictionary

def highest_bidder():
    highest_bid = 0
    for bidder in bid_dict:
        bid_amt = int(bid_dict[bidder])
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f"The winner is {winner} with bidding amount {highest_bid}")


# TODO-2: Save data into dictionary {name: price}
bid_dict={}
# TODO-3: Whether if new bids need to be added
bidder_avail=True
while bidder_avail:
    name = input("Whats your name: ")
    bid = input("Enter the bidding amount in $")
    bid_dict[name]=bid
    
    bidder_input=input("Is there another bidder available: Type yes or no:").lower()
    if bidder_input not in ("yes","no"):
           print("Invalid input, Type yes or no")
    elif bidder_input=="no":
            bidder_avail=False
            #print("Goodbye")
        
print(bid_dict) 
highest_bidder()        
    

            
