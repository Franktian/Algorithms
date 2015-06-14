'''Frank - my first dynamic programming function!!! and it's a linear time function fuck!!!!!!'''
def maxwt (inputArr):
    result = []
    result.append(0)
    result.append(inputArr[0])
    
    for i in range(1, len(inputArr)):
        result.append(max(result[i], result[i - 1] + inputArr[i]))
    print result
if __name__ == "__main__":
    arr = [1, 4, 5, 4, 6, 8]
    
    maxwt(arr)