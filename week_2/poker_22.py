import sys

possible_hands = [0] * 10
number_of_hands = 0
for line in sys.stdin:
   line = line.strip()
   rank = int(line[-1])
   possible_hands[rank] += 1
   number_of_hands += 1

prob_nothing = float((possible_hands[0] / number_of_hands) * 100)
prob_1_pair = float((possible_hands[1] / number_of_hands) * 100)
prob_2_pair = float((possible_hands[2] / number_of_hands) * 100)
prob_3_kind = float((possible_hands[3] / number_of_hands) * 100)
prob_straight = float((possible_hands[4] / number_of_hands) * 100)
prob_flush = float((possible_hands[5] / number_of_hands) * 100)
prob_house = float((possible_hands[6] / number_of_hands) * 100)
prob_4_kind = float((possible_hands[7] / number_of_hands) * 100)
prob_s_flush = float((possible_hands[8] / number_of_hands) * 100)
prob_r_flush = float((possible_hands[9] / number_of_hands) * 100)

print ('The probability of nothing is {:.4f}%'.format(prob_nothing))
print ('The probability of one pair is {:.4f}%'.format(prob_1_pair))
print ('The probability of two pairs is {:.4f}%'.format(prob_2_pair))
print ('The probability of three of a kind is {:.4f}%'.format(prob_3_kind))
print ('The probability of a straight is {:.4f}%'.format(prob_straight))
print ('The probability of a flush is {:.4f}%'.format(prob_flush))
print ('The probability of a full house is {:.4f}%'.format(prob_house))
print ('The probability of four of a kind is {:.4f}%'.format(prob_4_kind))
print ('The probability of a straight flush is {:.4f}%'.format(prob_s_flush))
print ('The probability of a royal flush is {:.4f}%'.format(prob_r_flush))
print (possible_hands)
print (number_of_hands)