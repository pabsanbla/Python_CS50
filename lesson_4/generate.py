import random
#from random import choice you take just that function
coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1,10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
