#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
x = [0]
w = []
y = []
z = [1.0/4,1.0/5,1.0/6,1.0/7,1.0/8]

a = []
b = []
c = []
d = []
e = []

if len(sys.argv) < 3:
	fin = open(sys.argv[1],"r")
	i = 4
	for line in fin:
		y.append(float(line))
	plt.figure(1)
	a = y[0]
	b = y[1]
	c = y[2]
	d = y[3]
	e = y[4]

	ax=plt.gca()  
	ax.set_xticks([0.5])
	ax.set_xticklabels((''))
	wideth = 0.15
	plt.bar([i+0.1 for i in x],a,wideth,None,color = 'r',label = 'ideal')
	plt.bar([i+0.25 for i in x],b,wideth,None,color = 'b',label = 'MTA-LDA')
	plt.bar([i+0.4 for i in x],c,wideth,None,color = 'g',label = 'MTA-LSA')
	plt.bar([i+0.55 for i in x],d,wideth,None,color = 'y',label = 'Simatt2')
	plt.bar([i+0.7 for i in x],e,wideth,None,color = 'c',label = 'Simatt')
	plt.ylabel('precision of attack',fontsize=30)
	plt.ylim([0,1])
	plt.xlim([0,1])
	for tick in ax.xaxis.get_major_ticks():
	    tick.label1.set_fontsize(20)
	for tick in ax.yaxis.get_major_ticks():
	    tick.label1.set_fontsize(20)
	plt.legend(loc = 1,ncol=3)

	plt.show()
