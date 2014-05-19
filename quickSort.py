def quickSort(lst):
    
    global c
    c = c + len(lst) - 1
    
    if len(lst) <= 1:
        return lst
    
    less = []
    equal = []
    greater = []
    pivot = lst[0]
    print "pivot: " + str(pivot)
    
    for item in lst:
        if item < pivot:
            less.append(item)
        if item == pivot:
            equal.append(item)
        if item > pivot:
            greater.append(item)
    return quickSort(less) + equal + quickSort(greater)

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 12]
    b = [6, 7, 8, 9, 10, 100]
    c = [10000, 967, 87, 91, 117, 819, 403, 597, 1201, 12090]
    d = [4, 3, 2, 1]
    

    
    c = 0
    quickSort(numbers)
    print c