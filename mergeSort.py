
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(lefthalf, righthalf, alist)
        
    print("Merging ",alist)
        


def merge (x, y, merged):
    '''
    Merge two integer list by descending order
    '''
    l = 0
    r = 0
    i = 0

    
    while l < len(x) and r < len(y):
        if x[l] < y[r]:
            merged[i] = x[l]
            l = l + 1
        else:
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
    c = [10000, 967, 87, 91, 117, 819, 403, 597, 1201, 12090]
    mergeSort(c)
