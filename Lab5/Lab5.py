import app
import utils

import numpy

x = input()
print(utils.process_item( int(x)))

app.func()



def prima():
    vowels = ['a', 'e', 'i','o','u','A', 'E', 'I','O','U']

    string_x = input()
    lst_string = list(string_x)

    return list(filter(lambda x : x in vowels ,lst_string))

def a_doua():
    vowels = ['a', 'e', 'i','o','u','A', 'E', 'I','O','U']

    string_x = input()
    lst_string = list(string_x)
    new_lst = [x for x in lst_string if x in vowels]
    return new_lst

def a_treia():
    vowels = ['a', 'e', 'i','o','u','A', 'E', 'I','O','U']

    string_x = input()
    lst_string = list(string_x)
    new_lst = []
    is_vowel = lambda x: x in vowels
    for x in lst_string:
        if is_vowel(x):
            new_lst.append(x)
    return new_lst

print(prima())
print(a_doua())
print(a_treia())

def my_function(*args,**kwargs):
    lst = []
    for x in args:
        if type(x) is dict:
            if len(x.keys()) >= 2:
                lista_key = x.keys()
                for cheie in lista_key:
                    if isinstance(cheie,str) and len(cheie) >=3:
                        lst.append(x)
                        break
    for key,value in kwargs.items():
        if type(value) is dict:
            if len(value.keys()) >= 2:
                lista_key_2 = value.keys()
                for cheie_2 in lista_key_2:
                    if isinstance(cheie_2,str) and len(cheie_2) >=3:
                        lst.append(value)
                        break
    return lst

print(my_function(
 {1: 2, 3: 4, 5: 6},
 {'a': 5, 'b': 7, 'c': 'e'},
 {2: 3},
 [1, 2, 3],
 {'abc': 4, 'def': 5},
 3764,
 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
 test={1: 1, 'test': True}
))

def my_function(lista):
    new_lst = []
    for x in lista:
        if type(x) == int or type(x) == float:
            new_lst.append(x)
    return new_lst

print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

def my_function(lista):
    lst = []
    lst_pos_even = []
    lst_pos_odd = []
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0 and i not in lst_pos_even:
            lst_pos_even.append(i)
            for j in range(0,len(lista)):
                if lista[j] % 2 != 0 and j not in lst_pos_odd:
                    lst_pos_odd.append(j)
                    lst.append([lista[i],lista[j]])
                    break
    return lst

print(my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

def f9(pairs = []):
    lst = []
    suma = 0
    prod = 1
    poww = 0
    for x in pairs:
        suma = x[0] + x[1]
        prod = x[0] * x[1]
        poww = pow(x[0],x[1])
        dict = {'sum' : suma, 'prod': prod, 'pow': poww}
        lst.append(dict.copy())
    return lst
print(f9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] ))