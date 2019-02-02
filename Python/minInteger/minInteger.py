# find the minimum positive integer that is NOT contained in a given array
# e.g. [1, 5, 2, 3] would give 4

def solution(A):
    # write your code in Python 3.6

    n=1
    i=0
    for i in range(len(A)):
        if(A[i]>=0):
            # split an array on the current element (one array of all values
            # before, and one array of all values after)
            B = A[0:i-1]
            C = A[i+1:]
            for item in C:
                B.append(item)

            # compare the array missing the 'current' index element to the
            # current 'minimum' integer
            for others in B:
                if(others==(n)):
                    # increment the minimum integer by 1 if any other array
                    # value matches it!
                    n=n+1
    print(n)
    return n
    pass

# test cases
solution([1, 3, 5, 7]) # 2
solution([1, 5, 2, 3]) # 4
solution([1, 5, 2, 3, 1, 3, 5, 7]) # 4
solution([7, 6, 5, 4]) # 1
solution([7, 6, 5, 4, 1, 2]) # 3
solution([1, 2]) # 3
solution([-1, 0, 1]) # 2
