from collections import Counter

#hands = ['TTTTT', '4444Q', '5KKK5', '55445', '7773J', '8855Q', 'KK123', '12345']


hands = ['5KKK5', '55445']

def get_hand_ranking(hand):
    """
    1: Five of a kind
    2: Four of a kind
    3: Full house
    4: Three of a kind
    5: Two pair
    6: One pair
    7: High card
    """
    card_counts = Counter(hand)
    max_occurrence = max(card_counts.values())
    print(card_counts)
    ranking_dict = {5: 1, 4: 2, 3: 3 if hand[0] == hand[-1] and len(set(hand[1:4])) == 1 else 4, 2: 5 if list(card_counts.values()).count(2) == 2 else 6}
    return ranking_dict.get(max_occurrence, 7)
"""
    print(list(card_counts.values()))
    print(hand[1:4])
    print(set(hand[1:4]))
    if max_occurrence == 5:
        return 1 # Five of a kind
    elif max_occurrence == 4:
        return 2 # Four of a kind
    elif max_occurrence == 3:
        if hand[0] == hand[-1] and len(set(hand[1:4])) == 1:
            return 3 # Full house
        else:
            return 4 # Three of a kind
    elif max_occurrence == 2:
        if list(card_counts.values()).count(2) == 2:
            return 5 # Two pair
        else:
            return 6 # One pair
    else:
        return 7 # High card
"""

for hand in hands:
    print(get_hand_ranking(hand))

