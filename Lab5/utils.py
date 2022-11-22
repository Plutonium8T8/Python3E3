def isPrime(x):
    if x < 2:
        return 0
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0
    for d in range(3,x, 2):
        if x % d == 0:
            return 0
    return 1

def process_item(x):
    q = x+1
    while (True):
        if isPrime(q):
            return q
        q = q+1
        
def main():
    print(process_item(100))
    
if __name__ == "__main__":
    main()