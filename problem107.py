'''
Problem Statement:
    Program to optimise the network by removing some edges and still ensure that all
    points on the network remain connected using the  minimum spanning tree algorithm

Author: Deepti Bhasin

References:
    http://en.wikipedia.org/wiki/Dtra%27s_algorithm
    http://www.tutorialspoint.com/python/
    https://docs.python.org/2.7/tutorial/index.html
'''

import csv
import sys
import time

orig_cost = 0
new_cost = 0
orig_tree = []
start_time = time.time()

try:
    f = open(sys.argv[1],"r")
except IOError:
    print "Cannot open file : %s" % (sys.argv[1])

f1 = csv.reader(f)

# Read the elements of input file in a list
i = 0
for row in f1:
    for x in row:
        orig_tree.append(x)
        if x != '-':
		    orig_cost += int(x)
    i += 1
num_of_nodes = i

# Initialize two lists - original list and new list to store the order of nodes reached
old_list = range(num_of_nodes)
new_list = []

# Insert first element from old list to new list (It can be initialized with any node in original list)

new_list.append(old_list[0])
old_list.remove(old_list[0])

# Remove items from old list and enter into new list. Hence run the program until old list is empty.
while (len(old_list)!=0):

    newindex = 0
    minimum = 99999 # minimum should be initialized to a higher value greater than cost of any existing edge
# Check condition for any entries in the list for '-' values
    for i in new_list:
        for j in old_list:
            if (orig_tree[i+j*num_of_nodes] != '-'):
# Compare costs for all elements in old list for every element in new list
                if (minimum > int(orig_tree[i+j*num_of_nodes])):
                    minimum = int(orig_tree[i+j*num_of_nodes])
                    newindex = j

    new_cost = new_cost+minimum
    new_list.append(newindex)
    old_list.remove(newindex)

original = orig_cost/2
saving = original - new_cost

print " Original Cost : %d" %original
print " New Cost : %d" %new_cost
print " Saving in Cost : %d" %saving
print("--- Time of execution : %s seconds ---" % (time.time() - start_time))
