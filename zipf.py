import matplotlib.pyplot as plt
import numpy as np

x = {}
for i in range(78774):
	tmp = np.random.zipf(1.04)
	if tmp in x:
		x[tmp] = x[tmp]+1
	else:
		x[tmp] = 1

for i in range(1,100):
	if i in x:
		print x[i]
	else:
		print 0

