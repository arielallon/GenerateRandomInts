#!/usr/bin/python

import bitvector
import sys
import random


def echo_unique_random_ints(lower_bound, upper_bound, total):
	"""Generates a list of unique integers in a random order.
	Will generate <total> numbers in the list, between <lower_bound> and <upper_bound>.

	Uses a bitvector to keep track of the numbers we've already generated to ensure uniqueness.
	Can get slower as it progresses if total is close to (upper_bound - lower_bound). 
	This is because it is increasingly likely to generate ints that are already in the bitvector 
	and have to try again. Need to figure out a different approach that doesn't have this issue.

	"""
	generated = bitvector.BitVector()
	count = 0

	while (count < total):
		num = random.randint(lower_bound,upper_bound)
		if not generated.get(num):
			print num
			generated.set(num)
			count += 1


if __name__ == "__main__":
	if len(sys.argv) != 4:
		print "Please call with the following structure:"
		print "generate_random_ints.py <lower_bound> <upper_bound> <total>"
		exit()
	
	lower_bound = int(sys.argv[1])
	upper_bound = int(sys.argv[2])
	total = int(sys.argv[3])

	# validation
	if lower_bound >= upper_bound:
		print "lower_bound must be less than upper_bound"
		exit()
	if (upper_bound - lower_bound) < total:
		print "total must be a number less than or equal to upper_bound minus lower_bound"
		exit()

	echo_unique_random_ints(lower_bound, upper_bound, total)