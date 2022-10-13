from numpy import place


def Ex1():
    number1 = input()
    number2 = input()

    number1 = int(number1)
    number2 = int(number2)

    while((number1 % number2) > 0):
        auxiliar = number1 % number2
        number1 = number2
        number2 = auxiliar

    return number2

def Ex2():
    string = input()
    count = 0
    for parser in string:
        if parser in "AaOoEeIiYyUu":
            count = count + 1
    return count

def Ex3(string1, string2):
    return string2.count(string1)

def Ex4():
    string = input()
    for parser in range(0, len(string)):
        if string[parser] in "QWERTYUIOPASDFGHJKLZXCVBNM":
            if(parser != 0):
                string = string[:parser] + "_" + string[parser].lower() + string[parser + 1:]
            else:
                string = string[:parser] + string[parser].lower() + string[parser + 1:]
    print(string)

def Ex5(arr, i, j, n, m):
    if i > n or j > m:
        return
    for p in range(i, m):
        print(arr[i][p], end="")
    for p in range(i + 1, n):
        print(arr[p][m - 1], end="")
    if (n - 1) != i:
        for p in range(m - 2, j - 1, -1):
            print(arr[n - 1][p], end="")
    if (m - 1) != j:
        for p in range(n - 2, i, -1):
            print(arr[p][j], end="")
    Ex5(arr, i + 1, j + 1, n - 1, m - 1)

n = int(input("Rows and colmuns:"))
matrix = []
for i in range(n):
    a=[]
    for j in range(n):
        a.append(input())
    matrix.append(a)

print("Your matrix: ")
for i in range(n):
    for j in range (n):
        print(matrix[i][j], end = "")
    print()

print("Spiral Order: ")
Ex5(matrix,0,0,n,n)

def Ex6():
    number = input()

    palindrome = True

    for parser in range(0, int(len(number) / 2)):
        if number[parser] != number[len(number) - parser - 1]:
            palindrome = False

    print(palindrome)

def Ex7(s):
    i = 0
    ok = False
    q=''
    for i in range(len(s)):
        while s[i].isdigit():
            ok = True
            q = q + s[i]
            if i == len(s)-1:
                return q
            i=i+1
        if ok:
            return q
    return q

s = input()
print(Ex7(s))

def Ex8():
    number = int(input())
    count = 0
    while number:
        if number & 1:
            count = count +1
        number = number >> 1
    print(count)

def Ex9():
    arr = [0] * 130
    s = input()
    s = s.lower().replace(' ','')
    max = 0
    maxCharacter = ''
    for x in s:
        arr[ord(x)] = arr[ord(x)] + 1
        if arr[ord(x)] > max:
            max = arr[ord(x)]
            maxCharacter = ord(x)

    print("The most common letter is:", chr(maxCharacter), ",", max ,"times")

def Ex10():
    s = input()
    print(len(s.split()))

