#!/usr/bin/python

import bitvector

import random

generated = bitvector.BitVector()
count = 0
total = 1000000

while (count < total):
	num = random.randint(0,total)
	if not generated.get(num):
		print num
		generated.set(num)
		count += 1

# write a file with all the numbers
# numbers = xrange(10000000, 99999999)
# for number in numbers:
# 	print number

# disadvantage is that removing elements is likely very slow.
# setting them to null as we go could result in plenty of false positives til we get them all
# num_remaining = len(numbers) - 1
# while num_remaining > 0:
# 	index = random.randint(0,num_remaining)
# 	print numbers[index]
# 	del(numbers[index])
# 	num_remaining -= 1