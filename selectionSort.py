def selectionSort(lst):
    
    for i in range(len(lst)):
        minimum = min(lst[i:])
        minimumIndex = lst[i:].index(minimum)
        
        lst[i + minimumIndex] = lst[i]
        lst[i] = minimum
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 12]
    b = [6, 7, 8, 9, 10, 100]
    c = [10000, 967, 87, 91, 117, 819, 403, 597, 1201, 12090]
    selectionSort(c)
    print c