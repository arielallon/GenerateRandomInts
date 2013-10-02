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
