import math
def karatuba (x, y):
    ''' 
    Python implementation of Karatuba algorithm
    Idea drives from the dicussion of Karatuba algorithm in Coursera
    Algorithms: Design and Analysis I(Stanford)
    For details please refer to the video
    @params: x, y are integers in string format
    returns the multiplication of x, y
    
    '''
    lenX = len(x)
    lenY = len(y)
    
    if (lenX == lenY and lenX == 1):
        return int(x) * int(y)
    
    # Balance x, y so that can be equally divided
    if (lenX > lenY):
        y = "0" + y
        half = int(lenX/2)
        leng = lenX
    elif (lenX < lenY):
        x = "0" + x
        half = int(lenY/2)
        leng = lenY
    else:
        half = int(lenX/2)
        leng = lenX
    
    a, b = x[:half], x[half:]
    c, d = y[:half], y[half:]
    
    return math.pow(10, 2*(leng - half)) * karatuba(a, c) + math.pow(10, leng - half) * (karatuba(a, d) + karatuba(b, c)) + karatuba(b, d)


    
if __name__ == "__main__":
    x = "543"
    y = "10"
    print karatuba(x, y)