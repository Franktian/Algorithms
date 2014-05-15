
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(lefthalf, righthalf, alist)
        
        


def merge (x, y, merged):
    '''
    Merge two integer list by descending order
    '''
    l = 0
    r = 0
    i = 0
    global c
    
    while l < len(x) and r < len(y):
        if x[l] < y[r]:
            merged[i] = x[l]
            l = l + 1
        else:
            c=c+len(x)-l #the maggic happens here
            merged[i] = y[r]
            r = r + 1
        i = i + 1
    
    while l < len(x):
        merged[i] = x[l]
        l = l + 1
        i = i + 1
    while r < len(y):
        merged[i] = y[r]
        r = r + 1
        i = i + 1

    
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 12]
    b = [6, 7, 8, 9, 10, 100]
    d = [5, 4, 3, 2, 1]
    c = 0
    mergeSort(d)
    print c
    print d
