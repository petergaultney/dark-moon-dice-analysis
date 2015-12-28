#!/usr/bin/env python

import sys
import itertools
from collections import defaultdict

black_d6 = [-2, -2, -2, -1, +2, +4]
red_d6 = [-2, -2, -2, -1, +1, +3]
blue_d6 = [-2, -2, -2, -1, +3, +5]

dice = {'black_d6': black_d6, 'red_d6': red_d6, 'blue_d6': blue_d6}

chosen_dice = list()

print('using dice: [ ', end='')
for arg in sys.argv[1:]:
    if arg not in dice:
        if arg == 'r':
            arg = 'red_d6'
        elif arg == 'k' or arg == 'b':
            arg = 'black_d6'
        elif arg == 'u' or arg == 'l' or arg == 'blue':
            arg = 'blue_d6'
    print(arg + ' ', end='')
    chosen_dice.append(dice[arg])
print(' ]')
    
rolls = list()

rolls = list(itertools.product(*chosen_dice))

roll_sum = 0
for roll in rolls:
    for die in roll:
        roll_sum += die
print('roll total avg: {:.2}'.format(roll_sum/len(rolls)))

from collections import defaultdict
nums_rolled = defaultdict(int)
for roll in rolls:
    for die in roll:
        nums_rolled[die] += 1

sorted_results = [res for res, count in nums_rolled.items()]
sorted_results.sort()
for res in sorted_results:
    print('{:+} was rolled {:.2} times on avg.'.format(res, nums_rolled[res]/len(rolls)))

one_or_more_positive = 0
num_positives = defaultdict(int)
for roll in rolls:
    how_many_pos = 0
    for die in roll:
        if die > 0:
            how_many_pos += 1
            if how_many_pos == 1:
                one_or_more_positive += 1
    num_positives[how_many_pos] += 1

more_than_one_positive_in_roll = 0
for num_pos, num in num_positives.items():
    print('{} positives in roll: {:.2%}'.format(num_pos, num/len(rolls)))
    if num_pos > 1:
        more_than_one_positive_in_roll += num
print('chance for one or more positives in roll: {:.2%}'.format(one_or_more_positive/len(rolls)))
print('chance for more than one positive in roll: {:.2%}'.format(more_than_one_positive_in_roll/len(rolls)))

positive_total = 0
avg_positive_dice = 0
times_with_no_positive_dice = 0
positive_rolls = list()
for roll in rolls:
    pos = 0
    for die in roll:
        if die > 0:
            pos += 1
            positive_total += die
            avg_positive_dice += 1
    if pos == 0:
        times_with_no_positive_dice += 1
    else:
        positive_rolls.append(pos)
print('avg # positive dice in roll: {:.2}'.format(avg_positive_dice/len(rolls)))
print('total positive roll expected: {:.2}'.format(positive_total/len(rolls)))
print('chance for no positive dice: {:.2%}'.format(times_with_no_positive_dice/len(rolls)))
positive_rolls.sort()
print('median positive roll: {}'.format(positive_rolls[len(positive_rolls)//2]))

best_sub_ooom = 0
most_common_best_roll_totals = defaultdict(int)
dice_submitted = defaultdict(int)
for roll in rolls:
    highest = -2
    roll_sub = 0
    for die in roll:
        if die > highest:
            highest = die
        if die > 0: # if positive
            roll_sub += die
    if roll_sub == 0:
        roll_sub = highest
    best_sub_ooom += roll_sub
    most_common_best_roll_totals[roll_sub] += 1
print('avg best roll sub: {:.3}'.format(best_sub_ooom/len(rolls)))

print('most common best roll subs: ')
lookup_by_count = dict()
for sub, ct in most_common_best_roll_totals.items():
    if ct not in lookup_by_count:
        lookup_by_count[ct] = list()
    lookup_by_count[ct].append(sub)
sorted_counts = sorted([count for count, subs in lookup_by_count.items()], reverse=True)
for count in sorted_counts:
    for sub in lookup_by_count[count]:
        print('{:+} results from {:.2%}'.format(sub, count/len(rolls)) + ' of rolls.')


