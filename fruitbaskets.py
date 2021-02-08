from itertools import combinations
from math import factorial
from sys import stdin

n = int(stdin.readline())
fruit_weights = list(map(int, stdin.readline().split()))
sum_weights = 0

#since the min fruit weight is 50,
#we only want to get combinations of length at MOST 4
max_comb = min(n, 3)
for i in range(1,max_comb+1):
    for c in combinations(fruit_weights, i):
        #add all combinations of sums if they're greater than 200
        if sum(c) >= 200:
            sum_weights += sum(c)
    i = i + 1


#now we add all combinations of length greater than 4 (if length is greater than 4)
for i in range(4, n + 1):
    for f in fruit_weights:
        sum_weights += ((factorial(n-1)) // ((factorial(i-1)) * (factorial((n-1)-(i-1)))))*f

print(sum_weights)

