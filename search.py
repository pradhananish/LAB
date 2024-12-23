import random
from binary import binary_search
from linear import linear_search
from time import time



#data = random.sample(range(100), 100)
input = 100000000000
data = range(input + 1)

k=12445
#Binary Search
start = time()
result_bin = binary_search(data,0,len(data)-1,k)
end = time()
time_bin = end-start
if result_bin != -1: 
    print("Element {} is  present in the array and time taken by binary search is {}".format(k,time_bin) ) 
else: 
    print("Element is not present in array")



#Linear Search
start = time()
result_lin = linear_search(data, k)
end = time()
time_lin = end-start

if result_lin != -1: 
    print("Element {} is  present in the array and time taken by linear search  is {}".format(k,time_lin) ) 
else: 
    print("Element is not present in array")
