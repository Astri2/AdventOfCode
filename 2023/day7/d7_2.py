f = open("day7/input.txt", "r")

def get_handpower(card_count: dict, card):
    J_nb = card_count.get('J', 0); card_count['J'] = 0
    card_count = sorted(card_count.values(), reverse=True)
    card_count[0] += J_nb
    if(card_count[0] == 5): hand_power = 7
    elif(card_count[0] == 4): hand_power = 6
    elif(card_count[0] == 3 and card_count[1] == 2): hand_power = 5
    elif(card_count[0] == 3): hand_power = 4
    elif(card_count[0] == card_count[1] == 2): hand_power = 3
    elif(card_count[0] == 2): hand_power = 2
    else: hand_power = 1
    return hand_power

order = "J23456789TQKA"

hands = []
for line in f.read().splitlines():
    hand_cards, bet = line.split()
    card_count = dict()
    hand_index = []
    for card in hand_cards:
        card_count[card] = card_count.get(card, 0) + 1
        hand_index.append(order.index(card))
    hand_power = get_handpower(card_count, hand_cards)
    hands.append((hand_power, hand_index, hand_cards, int(bet)))
    
hands.sort()
print(*hands,sep="\n")

score = sum([hand[3]*(i+1) for i, hand in enumerate(hands)])
print(score)
