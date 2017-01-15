#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
x = []
w = []
y = []
z = []

a = []
b = []
c = []
d = []
sum = 0
n = 0
i = 0
if len(sys.argv) < 3:
	fin = open(sys.argv[1],"r")
	for line in fin:
		i = i + 1
		line = line.strip('\n')
		x.append(int(line))
		n = n + int(line)
		sum = sum + int(line) * i
	plt.plot(x)
#	plt.xscale('log')
	plt.show()
	print sum
	print 1.0*n/i
	print i
	print n
	
