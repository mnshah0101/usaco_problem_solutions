import sys


k, n = [int(x) for x in input().split()]
if k == n:
    print(1)
    sys.exit()


points = [int(x) for x in input().split()]
confirmed_scores = [int(x) for x  in input().split()]
confirmed_set = set(confirmed_scores)


intial_score_guesses = set()



for final in confirmed_scores:
    running_sum = 0
    for point in points:
        running_sum += point
        initial = final - running_sum
        intial_score_guesses.add(initial)


confirmed = 0



for guess in intial_score_guesses:
    guess_sequence = set()
    initial = guess
    for point in points:
        initial += point
        guess_sequence.add(initial)
    
    if confirmed_set.issubset(guess_sequence):
        confirmed +=1

print(confirmed)



