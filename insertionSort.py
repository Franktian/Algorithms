def insertionSort(lst):
    for i in range(0, len(lst)):
        current = lst[i]
        j = i
        
        while j > 0 and lst[j - 1] > current:
            lst[j] = lst[j - 1]
            j = j - 1
        
        lst[j] = current
        
if __name__ == "__main__":
    d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    insertionSort(d)
    print d