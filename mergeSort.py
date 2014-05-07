def mergeSort(lst):
    '''
    Python implementation of recursive merge sort
    '''
    print "Splitting"
    print lst
    if (len(lst) > 1):
        half = int(len(lst) / 2)
        left = lst[:half]
        right = lst[half:]
        
        mergeSort(left)
        mergeSort(right)
        
        i = 0
        j = 0
        k = 0
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                lst[k]=left[i]
                i=i+1
            else:
                lst[k]=right[j]
                j=j+1
            k=k+1
            print lst
        
        while i<len(left):
            lst[k]=left[i]
            i=i+1
            k=k+1
            print lst

        while j<len(right):
            lst[k]=right[j]
            j=j+1
            k=k+1  
            print lst
        
    print "Merging"
    print lst

if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    mergeSort(alist)
    print alist