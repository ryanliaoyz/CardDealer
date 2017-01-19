from random import shuffle

suits = []
ranks = []

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(rank + ' ' + suit)

shuffle(deck)
print(deck)

hand1 = deck.pop() + ' ' + deck.pop() #remove the last one
hand2 = deck.pop() + ' ' + deck.pop()