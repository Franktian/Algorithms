
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)
        


def merge (x, y):
    '''
    Merge two integer list by descending order
    '''
    l = 0
    r = 0
    i = 0
    merged = []
    
    while l < len(x) and r < len(y):
        if x[l] < y[r]:
            merged.append(x[l])
            l = l + 1
        else:
            merged.append(y[r])
            r = r + 1
    
    while l < len(x):
        merged.append(x[l])
        l = l + 1
    while r < len(y):
        merged.append(y[r])
        r = r + 1

    
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 12]
    b = [6, 7, 8, 9, 10, 100]
    c = [10000, 967, 87, 91, 117, 819, 403, 597, 1201, 12090]
    mergeSort(c)
