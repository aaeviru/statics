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
if len(sys.argv) < 3:
	fin = open(sys.argv[1],"r")
	i = 4
	for line in fin:
		x.append(i)
		i = i+1
		y.append(float(line))
	plt.figure(1)
	ax=plt.gca()  
	ax.set_xticklabels(('4', '5', '6', '7','8','9','10'))
	plt.plot(x,y)
	plt.xlabel('BktSz',fontsize=30)
	plt.ylim([0.8,1])
	for tick in ax.xaxis.get_major_ticks():
	    tick.label1.set_fontsize(20)
	for tick in ax.yaxis.get_major_ticks():
	    tick.label1.set_fontsize(20)
	plt.show()
else:
	if int(sys.argv[2]) < int(sys.argv[3]):
		rr = [n for n in range(int(sys.argv[2]),int(sys.argv[3])+1)]
	else:
		rr = [n for n in range(int(sys.argv[2]),int(sys.argv[3])-1,-1)]		
	print rr
	for i in rr:
		fin = open(sys.argv[1]+str(i)+".txt","r")
		line = fin.readlines()
		linetmp = line[2].split()
		x.append(i)
		y.append((int(linetmp[2]))/2908.0)
		w.append((int(linetmp[1]))/2908.0)
		z.append((int(linetmp[0]))/2908.0)
		a.append((int(linetmp[2]))/2908000.0)
		b.append(1.0 * (int(linetmp[2])) / (int(linetmp[1])))
		c.append(1.0 * (int(linetmp[0])) / (int(linetmp[2])))
		d.append((int(linetmp[3]))/2908.0)
	plt.figure(1)
	plt.plot(x,y,label = 'hit')
	plt.plot(x,w,label = 'total')
#	plt.plot(x,z)
	plt.xlim(int(sys.argv[2]),int(sys.argv[3]))
	plt.legend(loc = 'best')
	plt.xlabel('number of terms')
	plt.ylabel('number of documents')
	plt.show()
	plt.figure(2)
	line1 = plt.plot(x,a,label = 'Recall')
	line2 = plt.plot(x,b,label = 'Precision')
#	line3 = plt.plot(x,d,label = 'Precision(fusion)')
	plt.legend(loc = 'best')
	plt.xlim(int(sys.argv[2]),int(sys.argv[3]))
	plt.ylim(0.0, 1.0)
	plt.xlabel('number of terms')
	plt.ylabel('number of documents')
	plt.show()
	plt.figure(3)
	plt.title('Fusion,K=60')
	plt.plot(x,z,label = 'hit')
	plt.legend(loc = 'best')
	plt.xlim(int(sys.argv[2]),int(sys.argv[3]))
	plt.xlabel('number of terms')
	plt.ylabel('number of documents')
	plt.show()
	plt.title('Fusion,K=60')
	plt.plot(x,d,label = 'hit in top20')
	plt.legend(loc = 'best')
	plt.xlim(int(sys.argv[2]),int(sys.argv[3]))
	plt.xlabel('number of terms')
	plt.ylabel('number of documents')
	plt.show()
	
