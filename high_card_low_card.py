import sys
sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")


def number_of_wins(bessie, elsie, cmp):
    # Determine sorting order:
    # If cmp(2,1) is True, then we’re using the ">" comparator (high-card wins)
    # and need to sort in descending order.
    if cmp(2, 1):
        bessie.sort(reverse=True)
        elsie.sort(reverse=True)
    else:
        # For the "lower card wins" case, sort in ascending order.
        bessie.sort()
        elsie.sort()

    wins = 0
    bpos = 0
    n_cards = len(bessie)
    for i in range(n_cards):
        # If Bessie's current card wins according to cmp, count a win and move to the next card.
        if cmp(bessie[bpos], elsie[i]):
            wins += 1
            bpos += 1
            if bpos == n_cards:  # If all of Bessie's cards are used, break early.
                break
    return wins


# Read input.
n = int(sys.stdin.readline())
elsie = [int(sys.stdin.readline()) for _ in range(n)]

# Split Elsie's plays into two halves.
elsie_first = elsie[:n // 2]
elsie_second = elsie[n // 2:]

# Determine Bessie's cards: all cards from 1 to 2n that Elsie doesn't have.
elsie_set = set(elsie)
bessie_first = []   # Cards to be used in the high-card-wins rounds.
bessie_second = []  # Cards to be used in the low-card-wins rounds.

# Fill Bessie's cards from highest to lowest.
for card in range(2 * n, 0, -1):
    if card not in elsie_set:
        if len(bessie_first) < n // 2:
            bessie_first.append(card)
        else:
            bessie_second.append(card)

# Compute wins for both halves.
wins = 0
wins += number_of_wins(bessie_first, elsie_first, lambda a, b: a > b)
wins += number_of_wins(bessie_second, elsie_second, lambda a, b: a < b)

sys.stdout.write(str(wins) + "\n")
