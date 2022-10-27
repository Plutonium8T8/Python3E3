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

Ex1()

def Ex2(list):
    prime = []
    for parser in list:
        if (sympy.isprime(parser)):
            prime.append(parser)

    print(prime)

Ex2([1,2,3,4,5,6,7,8,10])

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

    returnSet = set()
    returnSet.add(tuple(union))
    returnSet.add(tuple(intersection))
    returnSet.add(tuple(a_b))
    returnSet.add(tuple(b_a))

def Ex4(lst,moves,pos):
    if (pos >= 0 and pos < len(lst)):
        print(lst[pos])
        for x in moves:
            if abs(x) > len(lst):
                x = x % len(lst)
            pos = pos+x
            if pos > len(lst)-1:
                print(lst[pos - len(lst)])
            else:
                print(lst[pos])
    else:
        print("Start position invalid")

Ex4(["do", "re", "mi", "fa", "sol"], [1, -100, 14, 2], 2)

def Ex5(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j < i:
                matrix[i][j] = 0
n = 4
matrix = []
for i in range(n):
    a=[]
    for j in range(n):
        a.append(input())
    matrix.append(a)

Ex5(matrix)
print("Your matrix: ")
for i in range(n):
    for j in range (n):
        print(matrix[i][j], end = " ")
    print()

def not_in_lst(lst,x):
    if x in lst:
        return 0
    return 1

def Ex6(times, *args):
    lista=[]
    for list in args:
        for x in list:
            q=0
            for list2 in args:
                for y in list2:
                    if x == y:
                        q = q+1
            if q == times and not_in_lst(lista,x):
                lista.append(x)
    print(lista)
Ex6(2, [1,2,3,"cuvant"], [3,2,4,"altcuvant"],[4,5,6,1], [1,1, "cuvant"])

def palindrome(s):
    return s == s[::-1]

def Ex7(lst):
    count = 0
    big = 0
    for x in lst:
        if palindrome(str(x)):
            count = count + 1
            if x > big:
                big = x
    return [count,big]

print(Ex7([123, 1221, 11, 121]))

def Ex8(lista, x=1,flag = True):
    final_list = set()
    lst = []
    for word in lista:
        for character in word:
            if flag is True:
                if ord(character) % x == 0:
                    lst.append(character)
            elif flag is False:
                if ord(character) % x != 0:
                    lst.append(character)
        final_list.add(tuple(lst))
        lst.clear()
    return final_list

print(Ex8(["Exercitiu", "altcuvant", "calculator"], 2,False))

def Ex9(matrix):
    final_lst = set()
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(0, len(matrix[0])):
            for q in range(i-1,-1,-1):
                if matrix[i][j] <= matrix[q][j]:
                    final_lst.add(tuple([i,j]))
                    break
    return final_lst

p = [[1, 2, 3, 2, 1, 1],
     [2, 4, 4, 3, 7, 2],
     [5, 5, 2, 5, 6, 4],
     [6, 6, 7, 6, 7, 5]]

print(Ex9(p))

def Ex10(*lst):
    final_lst = set()
    lista = []
    test = 0
    for j in range(0, len(lst[test])):
        for i in range(0, len(lst)):
            if lst[i][j] is None:
                lista.append("None")
            else:
                lista.append(lst[i][j])
        final_lst.add(tuple(lista))
        lista.clear()
        test = test +1
    return final_lst

print(Ex10([1,2,3], [5,6,7], ["a", "b", "c"]))

def Ex11(my_list):
    my_list.sort(key=lambda x: x[1][2])
    return my_list


l = [['adc', 'bcd'], ['abc', 'zza'], ['abc', 'zzb']]
print(Ex11(l))

def Ex12(my_list):
    res = []
    formed_list = []

    my_list_aux = []

    for element in my_list:
        if element not in my_list_aux:
            my_list_aux.append(element)

    my_list = my_list_aux

    for word in my_list:
        formed_list = [word]
        for word2 in my_list:
            if word != word2 and word[-2:] == word2[-2:]:
                formed_list.append(word2)
        formed_list.sort()
        if formed_list not in res:
            res.append(formed_list)
    return res


a = ['cinci', 'trei', 'cinci', 'opinci', 'copac']
print(Ex12(a))