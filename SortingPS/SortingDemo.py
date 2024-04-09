# Bubble Sort
A = [5, 4, 1, 2, 7, 3, 6]

def BubbleSort(A): # O(N^2) worst case (reverse sorted input), O(N) best case (sorted input)
    N = len(A)
    while N > 1: # at most n-1 passes
        swapped = False
        for i in range(N-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i] # Python can swap variables like this
                swapped = True
        if not swapped: # optimization
            break
        N -= 1
    return A

print(A)
print(BubbleSort(A))

# Selection Sort
A = [5, 4, 1, 2, 7, 3, 6]

def SelectionSort(A): # O(N^2) for ALL cases...
    N = len(A)
    for L in range(N-1):
        smallest = A.index(min(A[L:N])) # BEWARE... this is O(N) not O(1)... we cannot find the smallest index of the minimum element of (N-L) items in O(1)
        A[smallest], A[L] = A[L], A[smallest] # Python can swap variables like this
    return A

print(A)
print(SelectionSort(A))

# Insertion Sort
A = [5, 4, 1, 2, 7, 3, 6]

def InsertionSort(A): # O(N^2) worst case (reverse sorted input), O(N) best case (sorted input)
    N = len(A)
    for i in range(1, N): # O(N)
        X = A[i] # X is the item to be inserted
        j = i-1
        while j >= 0 and A[j] > X: # can be fast or slow
            A[j+1] = A[j] # make a place for X
            j -= 1
        A[j+1] = X # index j+1 is the insertion point
    return A

print(A)
print(InsertionSort(A))

# Merge Sort
A = [5, 4, 1, 2, 7, 3, 6]

def MergeSort(A): # O(N log N) worst case for ALL cases :)
    N = len(A)
    if N == 1:
        return A

    mid = N//2
    left = A[:mid] # from start to before mid
    right = A[mid:] # from mid to end
    MergeSort(left) 
    MergeSort(right)

    i = j = k = 0
    while i < len(left) and j < len(right): # both left and right not empty
        if left[i] <= right[j]:
            A[k] = left[i] # take from left
            i += 1
        else:
            A[k] = right[j] # take from right
            j += 1
        k += 1
    while i < len(left): # has leftover from left (right is empty)
        A[k] = left[i]
        k += 1
        i += 1
    while j < len(right): # has leftover from right (left is empty)
        A[k] = right[j]
        k += 1
        j += 1
    return A

print(A)
print(MergeSort(A))













