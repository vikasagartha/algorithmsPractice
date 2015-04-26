import numpy as np
import time

def knapsackBruteForce(items, i, capacity):
    if i<0:
        return 0
    weight = items[i]['weight']
    value = items[i]['value']
    if weight > capacity:
        return knapsackBruteForce(items, i-1, capacity)
    else:
        return max(knapsackBruteForce(items, i-1, capacity), value + knapsackBruteForce(items, i-1, capacity - weight)) 

def knapsackDynamic(items, W):
    numItems = len(items)
    A = np.ones((W+1, numItems+1))
    A = A * -200

    #base case
    for capacity in range(0, W+1):
        A[capacity, 0] = 0

    for i in range(1, numItems+1):
        for capacity in range(0, W+1):
            value = items[i-1]['value']
            weight = items[i-1]['weight']
            if weight > capacity:
                A[capacity, i] = A[capacity, i-1] 
            else:
                A[capacity, i] = max(A[capacity, i-1], value + A[capacity-weight, i-1]) 
    return A[6, 4]

items = [] 
item = {'value': 3, 'weight': 4}
items.append(item)
item = {'value': 2, 'weight': 3}
items.append(item)
item = {'value': 4, 'weight': 2}
items.append(item)
item = {'value': 4, 'weight': 3}
items.append(item)

print "Solving knapsack problem for the following set of items: "
print items

start = time.time()
bruteForceResult = knapsackBruteForce(items, len(items)-1, 6)  
end = time.time()
bruteForceTime = end - start

start = time.time()
dynamicResult = knapsackDynamic(items, 6)
end = time.time()
dynamicTime= end - start

print "Brute Force time: ", bruteForceTime, ", Brute Force result: ", bruteForceResult 
print "Dynamic time: ", dynamicTime, ", Dynamic result: ", dynamicResult
