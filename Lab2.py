import sympy

def Ex1():
    n = 0
    while(n < 2):
        n = input()
        n = int(n)
    n1 = 1
    n2 = 1
    print("Fibonacci: ")
    print(1)
    print(1)
    for index in range(2,n):
        aux = n1
        n1 = n2
        n2 = aux + n2
        print(n2)

def Ex2(list):
    prime = []
    for parser in list:
        if (sympy.isprime(parser)):
            prime.append(parser)

    print(prime)

# Ex2([1,2,3,4,5,6,7,8,10])

def Ex3():
    a = input()
    b = input()

    union = []
    intersection = []
    a_b = []
    b_a = []

    for parser1 in a:
        for parser2 in b:
            if (parser1 == parser2):
                union.append(parser1)
            if (parser1 != parser2 and parser1 not in intersection):
                intersection.append(parser1)
            if (parser1 != parser2 and parser2 not in intersection):
                intersection.append(parser2)
            if (parser1 not in b and parser1 not in a_b):
                a_b.append(parser1)
            if (parser2 not in a and parser2 not in b_a):
                b_a.append(parser2)

    print(union)
    print(intersection)
    print(a_b)
    print(b_a)

Ex3()