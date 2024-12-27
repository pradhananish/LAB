import random
from lab1.binary import binary_search
from lab1.linear import linear_search
from time import time
from matplotlib import pyplot as plt 


time_linear = []
time_binary = []
x_val = []

time_lin = 0.00
time_bin = 0.00
for i in range(10000,100000+1,10000):
    input = i
    data = range(input + 1)
    k=i-1
    x_val.append(i)
    start = time()
    result_lin = linear_search(data, k)
    end = time()
    time_lin = end-start
    time_linear.append(time_lin)


    start = time()
    result_bin = binary_search(data,0,len(data)-1,1)
    end = time()
    time_bin = end-start
    time_binary.append(time_bin)


fig, ax = plt.subplots()
ax.plot(x_val,time_linear,'red',label='Linear Search')
ax.plot(x_val,time_binary,'blue',label='Binary Search')
plt.suptitle('Worst Case Time Complexity')
plt.xlabel('No of Data')
plt.ylabel('Time in seconds')
plt.legend()
plt.show()