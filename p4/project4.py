"""
Math 560
Project 4
Fall 2021

Partner 1:
Partner 2:
Date:
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')

    # fill the DP table
    dp = [[[0, '-'] for j in range(len(dest)+1)] for i in range(len(src)+1)]
    # fill base cases first
    for j in range(1, len(dest)+1):
        if prob == 'ASM':
            dp[0][j][0] = 0
            dp[0][j][1] = 'x'
        else:
            dp[0][j][0]=j
            dp[0][j][1]='L'
    for i in range(1, len(src)+1):
            dp[i][0][0]=i
            dp[i][0][1]='U'
    # fill blanks according to known values
    for i in range(1,len(src)+1):
        for j in range(1,len(dest) + 1):
            if src[i-1]==dest[j-1]:
                dp[i][j][0]=dp[i-1][j-1][0]
                dp[i][j][1]='D'
            else:
                dp[i][j]=min_case(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

    # reconstruct the solution
    edits = []
    i=len(src)
    j=len(dest)
    while (dp[i][j][0]!=0):
        if dp[i][j][1] == 'L':
            edits += [('insert', dest[j - 1], i)]
            j -= 1
        elif dp[i][j][1] == 'U':
            edits += [('delete', src[i - 1], i - 1)]
            i -= 1
        else:
            if src[i-1]==dest[j-1]:
                edits += [('match',dest[j-1],i-1)]
            else:
                edits += [('sub', dest[j - 1], i - 1)]
            i -= 1
            j -= 1
    dist = dp[len(src)][len(dest)][0]
    return dist, edits

def min_case(a,b,c):
    min_op = min(a[0],b[0],c[0])
    if b[0]==min_op:
        return [min_op+1, 'L']
    if a[0]==min_op:
        return [min_op+1, 'U']
    if c[0]==min_op:
        return [min_op+1,'D']

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 1, 5, 'ASM')
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')