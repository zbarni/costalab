#!/usr/bin/python

import sys

if len(sys.argv) < 2:
	print "must provide at least 1 .data file"
	exit(1)

for filename in sys.argv[1:]:
	A = 0
	T = 0
	C = 0
	G = 0
	CpG = 0
	tot = 0
	with open(filename, "r") as f:
		for line in f:
			if line[0] == '#' or line[0] == ' ':
				continue

			motif = line.split()[0]

			prev = "X"
			for c in motif:
				if c == "A":
					A += 1
				elif c == "T":
					T += 1
				elif c == "C":
					C += 1
				elif c == "G":
					G += 1
					if prev == "C":
						CpG += 1

				if c != "N":
					tot += 1
				
				prev = c

	print filename
	GC = C+G
	print "tot:", tot, "GC%", (float(GC) / tot) * 100.0, "CpG%", (float(CpG) / (tot - 1)) * 100.0
	GC = G + C
	GC_perc = 0 if tot == 0 else (float(GC) / tot) * 100.0
	CpG_perc = 0 if tot == 0 else (float(CpG) / tot) * 100.0
	print "GC%", GC_perc, "CpG%", CpG_perc, "A:", A, "T:", T, "C:", C, "G:", G, "TOT:", tot
