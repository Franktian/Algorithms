def bubbleSort(lst):
    '''
    Standard bubble sort implementation
    '''
    sort = False
    
    while not sort:
        sort = True
        i = 0
        while i < len(lst) - 1:
            if lst[i] > lst[i + 1]:
                sort = False
                temp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = temp
            i = i + 1

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 12]
    b = [6, 7, 8, 9, 10, 100]
    c = [10000, 967, 87, 91, 117, 819, 403, 597, 1201, 12090]
    d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubbleSort(d)
    print d
