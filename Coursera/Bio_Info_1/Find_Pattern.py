#!/Users/varamesh/anaconda/bin/python3

import sys

lines = sys.stdin.read().splitlines()

sequence = lines[0]
size = int(lines[1])

def PatternCount (seq, pat):

	count = 0

	for i in range(0, len(seq) - len(pat) + 1):
		if (seq[i:i+len(pat)] == pat):
			count = count + 1

	return count


def FrequentWords (seq, size):

	FrequentPat = set()
	count = list()
	maxcount = 0

	for i in range(0, len(seq) - size + 1):
		
		count.append(PatternCount(seq, seq[i:i+size]))
		if (count[i] > maxcount):
			maxcount = count[i]

	for i in range(0, len(seq) - size + 1):

		if(count[i] == maxcount):
			FrequentPat |= { seq[i:i+size] }

	return FrequentPat


# print(PatternCount(sequence,pattern))

print(" ".join(FrequentWords(sequence, size)))