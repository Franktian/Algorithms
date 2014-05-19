def partitionFirst(A, l, r):
    global e
    e += r - l
    
    pivot = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i = i + 1
    A[l], A[i - 1] = A[i - 1], A[l]

    return i - 1

def partitionEnd(A, l, r):
    global f
    f += r - l
    
    A[l], A[r] = A[r], A[l] # swap the last with the first
    pivot = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i = i + 1
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1

def partitionMedian(A, l, r):

    
    determineMedian(A, l, r) # determine and swap
    global g
    g += r - l    
    pivot = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i = i + 1
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1

    

def determineMedian(A, l, r):
    '''Determine who should be the pivot and switch with the first'''
    length = r - l + 1
    
    first = A[l]
    last = A[r]
    
    if length % 2 == 0:
        middleIndex = (l + r + 1) / 2 - 1
        middle = A[middleIndex]
    else:
        middleIndex = (l + r) / 2
        middle = A[middleIndex]
    
    
    lst = []
    lst.append(first)
    lst.append(middle)
    lst.append(last)
    

    
    lst.sort()
    
    if (lst[1] == A[l]):
        median = l
    elif (lst[1] == A[middleIndex]):
        median = middleIndex
    else:
        median = r
    A[l], A[median] = A[median], A[l]

    

def quicksort(myList, start, end):
    if start < end:
        pivot = partitionMedian(myList, start, end)
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList



if __name__ == "__main__":
    
    f = open('QuickSort.txt')
    
    numbers = []
    line = f.readline()
    while(line):
        numbers.append(int(line))
        line = f.readline()
    f.close()

    e = 0
    f = 0
    g = 0
    
    #b = [8, 7, 6, 5, 4, 3, 2, 9]
    #determineMedian(b, 0, len(b) - 1)
    #print b
    
    b = quicksort(numbers, 0, len(numbers) - 1)
    print "first: " + str(e)
    print "last: " + str(f)
    print "median: " + str(g)
    
    
# pivot first: 162085
# pivot last: 164123
# pivot median: 138382