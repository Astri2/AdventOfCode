f = open("day7/input.txt", "r")

def get_handpower(hand_power, card):
    hand_power = sorted(hand_power.values(), reverse=True)
    if(hand_power[0] == 5): hand_power = 7
    elif(hand_power[0] == 4): hand_power = 6
    elif(hand_power[0] == 3 and hand_power[1] == 2): hand_power = 5
    elif(hand_power[0] == 3): hand_power = 4
    elif(hand_power[0] == hand_power[1] == 2): hand_power = 3
    elif(hand_power[0] == 2): hand_power = 2
    else: hand_power = 1
    return hand_power

order = "23456789TJQKA"

hands = []
for line in f.read().splitlines():
    cards, bet = line.split()
    hand_power = dict()
    hand_index = []
    for c in cards:
        hand_power[c] = hand_power.get(c, 0) + 1
        hand_index.append(order.index(c))
    hand_power = get_handpower(hand_power, cards)
    hands.append((hand_power, hand_index, cards, int(bet)))
hands.sort()
print(*hands[::-1],sep="\n")

score = sum([hand[3]*(i+1) for i, hand in enumerate(hands)])
print(score)