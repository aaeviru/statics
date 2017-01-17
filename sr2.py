#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
x = [3,7]
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
	#c = y[4:6]

	ax=plt.gca()  
	ax.set_xticks(x)
	#ax.set_xticklabels(('3','7'))
	wideth = 0.15
	#plt.plot(x,a,'yo-',label = 'HDGA')
	plt.plot(x,a,'bo-',label = 'QO')
	plt.plot(x,b,'go-',label = 'QO2')
	plt.plot(x,[1.0/4,1.0/8],'ro-',label = 'ideal')
	#plt.bar([i+0.55 for i in x],d,wideth,None,color = 'y',label = 'cos-near')
	#plt.bar([i+0.7 for i in x],e,wideth,None,color = 'c',label = 'cos-far')
	plt.ylabel('precision of attack',fontsize=30)
	plt.xlabel('number of dummy query',fontsize=30)
	plt.ylim([0,1])
	plt.xlim(x)
	for tick in ax.xaxis.get_major_ticks():
	    tick.label1.set_fontsize(20)
	for tick in ax.yaxis.get_major_ticks():
	    tick.label1.set_fontsize(20)
	plt.legend(loc = 4,ncol=3)

	plt.show()
