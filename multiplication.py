import math
def karatuba (x, y):
    ''' Python implementation of Karatuba algorithm
    @params: x, y are n digits integers
    '''
    lenX = len(x)
    lenY = len(y)
    
    if (lenX == lenY and lenX == 1):
        return int(x) * int(y)
    
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
    y = "123"
    print karatuba(x, y)