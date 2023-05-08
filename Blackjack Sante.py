import random


# The Card class definition
class Card:
    def __init__(self, suit, value, card_value):
        # Färg
        self.suit = suit

        # Nummer på kortet
        self.value = value

        # Värdet
        self.card_value = card_value


# gör korten
def print_cards(cards, hidden):
    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == "10":
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|       {}       |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == "10":
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)

    print()


def blackjack_game(deck):
    # Spelarens och utdelarns kort
    player_cards = []
    dealer_cards = []

    # Spelarens och utdelarns poäng
    player_score = 0
    dealer_score = 0

    # Första korten till spelaren och utdelarn
    while len(player_cards) < 2:

        # Ger ett kort från kortleken
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
        player_score += player_card.card_value

        # Om båda har Ess görs det första Esset till en 1
        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

        # Printa spelarens kort och poäng
        print("PLAYER CARDS: ")
        print_cards(player_cards, False)
        print("PLAYER SCORE = ", player_score)

        input()

        # Ger ett kort från kortleken
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
        dealer_score += dealer_card.card_value

        # Printar utdelarens kort och poäng med det sita kortet gömt
        print("DEALER CARDS: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("DEALER SCORE = ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

        # Om båda korten är Ess görs den ena till värdet 1
        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10

        input()

    # Spelaren får Blackjack
    if player_score == 21:
        print("PLAYER HAS A BLACKJACK!!!!")
        print("PLAYER WINS!!!!")
        quit()

    # Printa spelaren och utdelarens kort
    print("DEALER CARDS: ")
    print_cards(dealer_cards[:-1], True)
    print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

    print()

    print("PLAYER CARDS: ")
    print_cards(player_cards, False)
    print("PLAYER SCORE = ", player_score)

    # Ser vad spelaren vill göra
    while player_score < 21:
        choice = input("Enter H to Hit or S to Stand : ")

        # Kollar att inputen är okej
        if len(choice) != 1 or (choice.upper() != "H" and choice.upper() != "S"):
            print("Wrong choice!! Try Again")

        # Om spelaren vill ha ett till kort
        if choice.upper() == "H":

            # Ger ett nytt kort
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)

            # Updating player score
            player_score += player_card.card_value

            # Updaterar spelarns poäng ifall spelarn har Ess
            c = 0
            while player_score > 21 and c < len(player_cards):
                if player_cards[c].card_value == 11:
                    player_cards[c].card_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1

            # Printa spelaren och utdelarens kort
            print("DEALER CARDS: ")
            print_cards(dealer_cards[:-1], True)
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

            print()

            print("PLAYER CARDS: ")
            print_cards(player_cards, False)
            print("PLAYER SCORE = ", player_score)

        # Om spelaren inte vill ha fler kort
        if choice.upper() == "S":
            break

    # Printa spelaren och utdelarens kort
    print("PLAYER CARDS: ")
    print_cards(player_cards, False)
    print("PLAYER SCORE = ", player_score)

    print()
    print("DEALER IS REVEALING THE CARDS...")

    print("DEALER CARDS: ")
    print_cards(dealer_cards, False)
    print("DEALER SCORE = ", dealer_score)

    # Kolla om spelaren har Blackjack
    if player_score == 21:
        print("YOU WIN, PLAYER HAS A BLACKJACK!!!")
        quit()

    # Kollar om spelarn har över 21
    if player_score > 21:
        print("HOUSE WINS, PLAYER BUSTED")
        quit()

    input()

    # Hanterar utdelarns val
    while dealer_score < 17:

        print("DEALER DECIDES TO HIT.....")

        # Ger delearn kort
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
        dealer_score += dealer_card.card_value

        # Hanterar Ess
        c = 0
        while dealer_score > 21 and c < len(dealer_cards):
            if dealer_cards[c].card_value == 11:
                dealer_cards[c].card_value = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1

        # Prinar spelarn och utdelarns kort
        print("PLAYER CARDS: ")
        print_cards(player_cards, False)
        print("PLAYER SCORE = ", player_score)

        print()

        print("DEALER CARDS: ")
        print_cards(dealer_cards, False)
        print("DEALER SCORE = ", dealer_score)

        input()

    # Utdelarn förlorar
    if dealer_score > 21:
        print("YOU WIN, DEALER BUSTED")
        quit()

    # Utdelarn får Blackjack
    if dealer_score == 21:
        print("HOUSE WINS, DEALER HAS GOTTEN BLACKJACK")
        quit()

    # Oavgjort
    if dealer_score == player_score:
        print("HOUSE WINS, TIE GAME")

    # Spelarn vinner
    elif player_score > dealer_score:
        print("YOU WIN, HIGHER SCORE")

    # Utdelarn vinner
    else:
        print("YOU LOSE, LOWER SCORE")


if __name__ == "__main__":

    # Färg
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

    # Printas på kortet
    suits_values = {
        "Spades": "\u2664",
        "Hearts": "\u2661",
        "Clubs": "\u2667",
        "Diamonds": "\u2662",
    }

    # Värdet som printas på koret
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # Kortets värde
    cards_values = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }

    # Tom kortlek
    deck = []

    # Loop för alla färger
    for suit in suits:

        # Loop för korets färg värde
        for card in cards:
            # lägger in korten in kortleken
            deck.append(Card(suits_values[suit], card, cards_values[card]))

    blackjack_game(deck)
