#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
x = [3,4,5,6,7]
w = []
y = []
z = [1.0/4,1.0/5,1.0/6,1.0/7,1.0/8]

a = []
b = []
c = []
d = []
if len(sys.argv) < 3:
	fin = open(sys.argv[1],"r")
	i = 4
	for line in fin:
		y.append(float(line))
	plt.figure(1)
	w = y[:5]
	y = y[5:]
	ax=plt.gca()  
	ax.set_xticks(x)
	#ax.set_xticklabels(('3','','4','','5','','6','','7'))

	plt.plot(x,w,'o-',label = 'LSA')
	plt.plot(x,y,'o-',label = 'LDA')
	plt.plot(x,z,'ro-',label = 'ideal value')
	plt.xlabel('number of dummy query',fontsize=30)
	plt.ylabel('precision of attack',fontsize=30)
	plt.ylim([0,1])
	for tick in ax.xaxis.get_major_ticks():
	    tick.label1.set_fontsize(20)
	for tick in ax.yaxis.get_major_ticks():
	    tick.label1.set_fontsize(20)
	plt.legend(loc = 'best')

	plt.show()
