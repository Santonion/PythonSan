import random

#part 1
#Sätter in suit och value i class man behåller namn
class Card:
    def __init__(self, suits, values, numbers):
        self.suit = suits
        self.value = values
        self.number = numbers

suit = ["Clubs", "Diamonds" "Hearts", "Spades"]
number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
value = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
print = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}


deck = []
#tom kortlek
for suits in suit:
    for cards in number:
#lopar suit och card
        deck.append(Card(print[suits], cards, value[cards]))


#part 2
player_cards = []
dealer_cards = []
#båda har inga kort
player_score = 0
dealer_score = 0
#båda har inga poäng

while len(player_cards) < 2:
    player_card = random.choice(deck)
    player_cards.append(player_card)
#lägger in card i cards, lägger altså in ett kort i handen med flera kort
    deck.remove(player_card)
#ger spelarn ett kort
    player_score += value
    if len(player_cards) == 2:
        if player_cards[0].value == 11 and player_cards[1].value == 11:
            player_cards[0].value = 1
            player_score -= 10