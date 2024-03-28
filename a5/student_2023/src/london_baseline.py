# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

with open('birth_dev.tsv', encoding='utf-8') as fin:
    lines = [x.strip().split('\t') for x in fin]
predictions = ['London'] * len(lines)
total, correct = utils.evaluate_places('birth_dev.tsv', predictions)
print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))