def inversions(lst):
    inversions = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                inversions += 1
    print "N^2: " + str(inversions)

def merge(A,B):
    global c
    C=[]
    lenA=len(A)
    lenB=len(B)
    i=0
    j=0
    while i<lenA and j<lenB:
        if A[i]<=B[j]:
            C.append(A[i])
            i=i+1
        else:
            c=c+len(A)-i #the maggic happens here
            C.append(B[j])
            j=j+1
    if i==lenA:#A get to the end
        C.extend(B[j:])
    else:
        C.extend(A[i:])
    return C

def mergeSort(L):
    N=len(L)
    if N>1:
        S1=mergeSort(L[0:N/2])
        S2=mergeSort(L[N/2:])
        return merge(S1,S2)
    else:
        return L

if __name__ == "__main__":
    a = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
    b = [5, 4, 3, 2, 1]

    f = open('integerArray.txt')

    numbers = []
    line = f.readline()
    while(line):
        numbers.append(int(line))
        line = f.readline()
    f.close()
    
    print len(numbers)

    print "start"
    c = 0
    mergeSort(numbers)
    print "NLogN: " + str(c)

#2412896071 - lines - correct
#2430156032
# 2407905288 - after test file passed