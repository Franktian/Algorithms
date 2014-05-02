import math
def karatuba (x, y):
    ''' Python implementation of Karatuba algorithm
    @params: x, y are n digits integers
    '''
    n = len(x)
    
    if (n == 1):
        return int(x) * int(y)
    
    #firstpart, secondpart = string[:len(string)/2], string[len(string)/2:]
    a, b = x[:n/2], x[n/2:]
    c, d = y[:n/2], y[n/2:]
    return math.pow(10, n) * karatuba(a, c) + math.pow(10, n/2) * (karatuba(a, d) + karatuba(b, c)) + karatuba(b, d)
    
if __name__ == "__main__":
    x = "56"
    y = "12"
    print karatuba(x, y)