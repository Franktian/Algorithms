def quickSort(lst):
    if len(lst) <= 1:
        return lst
    
    less = []
    equal = []
    greater = []
    pivot = lst[0]
    
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
    d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1]
    d = quickSort(d)
    print d