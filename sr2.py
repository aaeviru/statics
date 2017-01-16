#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
x = [0,1]
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
	a = y[:2]
	b = y[2:4]
	c = y[4:6]
	d = y[6:8]
	e = y[8:]

	ax=plt.gca()  
	ax.set_xticks([0.5,1.5])
	ax.set_xticklabels(('LDA(min)','LSA(max)'))
	wideth = 0.15
	plt.bar([i+0.1 for i in x],a,wideth,None,color = 'r',label = 'random')
	plt.bar([i+0.25 for i in x],b,wideth,None,color = 'b',label = 'coef-near')
	plt.bar([i+0.4 for i in x],c,wideth,None,color = 'g',label = 'coef-far')
	plt.bar([i+0.55 for i in x],d,wideth,None,color = 'y',label = 'cos-near')
	plt.bar([i+0.7 for i in x],e,wideth,None,color = 'c',label = 'cos-far')
	plt.ylabel('precision of attack',fontsize=30)
	plt.ylim([0,1])
	plt.xlim([0,2])
	for tick in ax.xaxis.get_major_ticks():
	    tick.label1.set_fontsize(20)
	for tick in ax.yaxis.get_major_ticks():
	    tick.label1.set_fontsize(20)
	plt.legend(loc = 'best',ncol=2)

	plt.show()
