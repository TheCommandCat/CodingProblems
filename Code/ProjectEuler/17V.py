'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

'''

import num2words

x = 0

for i in range(1, 1001):
    numstr = num2words.num2words(i).replace('-', '').replace(' ', '')
    x += len(numstr)
print(x)
