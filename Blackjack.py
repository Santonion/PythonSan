class deck:
    suit = ['Clubs"', 'Diamonds' 'Hearts', 'Spades']
    value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []
    for suit in suit:
        for value in value:
            deck.append(suit + value)

    clubs = []
    diamond = []
    heart = []
    spade = []

    for suit in suit:
        for value in value:
            if suit == "Clubs":
                clubs.append(suit + value)
            elif suit == "Diamonds":
                clubs.append(suit + value)
            elif suit == "Hearts":
                clubs.append(suit + value)
            else:
                clubs.append(suit + value)

print(deck)