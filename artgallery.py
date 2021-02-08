from sys import stdin
import pprint

left = 0
right = 1
inf = 10000000000

line = stdin.readline().split()
n = int(line[0])
num_closed = int(line[1])

#return N x 2 array of given art gallery
gallery = [x.rstrip().split() for x in stdin.readlines()]
del gallery[-1]

seen = [[[None for k in range(2)] for j in range(n)] for i in range(num_closed + 1)]

def recurse_column(k, r, c):
    if k == 0:
        return 0
    elif r < 0 or k < 0:
        return inf
    elif seen[k][r][c] != None:
        return seen[k][r][c]
    #check if we have already seen this partial state
    else:
    #otherwise, calculate minimum region starting at current cell
        tmp_val = int(gallery[r][c])
        seen[k][r][c] = min(
            tmp_val + recurse_column(k - 1, r - 1, c),
            recurse_gallery(k, r - 1)
        )
        return seen[k][r][c]


#
def recurse_gallery(k, r):
    #we return the minimum sumed values from the left and right columms
    return min(recurse_column(k, r, left),recurse_column(k, r, right))


#sum total rooms in the gallery with all of them open
def sum_gallery():
    sum_values = 0
    for i in range(0, n):
        sum_values += int(gallery[i][left]) + int(gallery[i][right])
        #from our total sum, we'll subtract the minimum cost we can obtain
        #by recursing through the gallery
    return sum_values - recurse_gallery(num_closed, n-1)


print(sum_gallery())



