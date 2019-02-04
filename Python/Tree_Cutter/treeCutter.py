# Find the number of trees that can be cut down from a line of trees, where
# each consecutive tree must be the same height or taller than the one
# before it!


# function to tell if the tree line meets the condition described
def testTreeLine(A):
    height = A[0]
    for i in range(len(A)):
        if i==0:
            pass
        elif i>0:
            if(A[i-1]>=height):
                height = A[i-1]
            if height>A[i]:
                return False
    return True

# make array A append all elements of array B
def combineArrays(A, B):
    for item in B:
        A.append(item)
    return A

# check if solution is possible
def impossible(A):
    maxIndex = A.index(max(A))
    maxBefore = max(A[0:maxIndex])
    minAfter = min(A[maxIndex:])
    if (minAfter<=(maxBefore-2) and len(A[maxIndex:])>1):
        return True
    else:
        return False

# function to see how many trees can be cut down
def numCutTrees(A):
    n=0
    # check case where no solutions possible
    #if impossible(A):
    #    return n

    for l in range(len(A)):
        if l==0:
            D = A[1:]
        elif l==len(A)-1:
            D = A[0:l]
        else:
            B = A[0:l]
            C = A[l+1:]
            D = combineArrays(B, C)
            #print(D)

        if(testTreeLine(D)):
            n=n+1

    return n


N = [1, 2, 3, 4, 4] # 5
L = [1, 4, 2, 3] # 1
C = [1, 3, 5, 3] # 2
D = [1, 4, 3, 5, 3] # 0
E = [1, 2, 3, 4, 1] # 1

print(numCutTrees(N))
print(numCutTrees(L))
print(numCutTrees(C))
print(numCutTrees(D))
print(numCutTrees(E))
