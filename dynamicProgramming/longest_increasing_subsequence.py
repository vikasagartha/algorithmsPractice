import time
import numpy as np

def LISBruteForce(A, i, j):
    if j > len(A)-1:
        return 0
    elif A[i]>A[j]:
        return LISBruteForce(A, i, j+1)
    else:
        return max(LISBruteForce(A, i, j+1), 1+LISBruteForce(A, j, j+1))

def LISDynamic(A):
    A = [-1000] + A
    length = len(A)
    M = np.ones((length, length+1)) 

    #base cases, j > length
    for i in range(length):
        M[i][length] = 0

    for i in range(length-1, -1, -1):
        for j in range(length-1, 0, -1):
            if A[i]>A[j]:
                M[i][j] = M[i][j+1]
            else:
                M[i][j] = max(M[i][j+1], 1+M[j][j+1])

    return M[0][1]

nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print "Computing longest increasing subsequence of ", nums

start = time.time()
bruteForceResult = LISBruteForce(nums, 0, 0)
end = time.time()
bruteForceTime = end - start

start = time.time()
dynamicResult = LISDynamic(nums)
end = time.time()
dynamicTime= end - start

print "Brute Force time: ", bruteForceTime, ", Brute Force result: ", bruteForceResult 
print "Dynamic time: ", dynamicTime, ", Dynamic result: ", dynamicResult
