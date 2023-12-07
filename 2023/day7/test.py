from collections import Counter

hands = ['TTTTT', '4444Q', '5KKK5', '7773J', '8855Q', 'KK123', '12345']

def get_hand_ranking(hand):
    card_counts = Counter(hand)
    max_occurrence = max(card_counts.values())
    ranking_dict = {5: 1, 4: 2, 3: 3 if hand[0] == hand[-1] else 4, 2: 5 if list(card_counts.values()).count(2) == 2 else 6}
    return ranking_dict.get(max_occurrence, 7)

for hand in hands:
    print(get_hand_ranking(hand))
