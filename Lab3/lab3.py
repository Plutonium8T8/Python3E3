#ex2

def dictionar (word):
    dic ={}
    for i in word:
        if i in dic:
            dic[i] = dic[i] +1
        else:
            dic.update({i : 1})
    return dic

test = dictionar("Ana has apples.")
print(test)

#ex3
def dic_eqls (dic1, dic2):
    if len(dic1) != len(dic2):
        return 0
    for i in dic1:
        if dic1.get(i) != dic2.get(i):
            return 0
        if dic1.get(i) is dict and dic2.get(i) is dict:
            return dic_eqls(dic1.get(i), dic2.get(i))
        else:
            return 0
    return 1


dict1 = {'Name': 'Cristian', 'Age': 2, "x" : {"x" : 1}}
dict2 = {'Name': 'Cristian', 'Age': 2, "x" : {"x" : 1}}

print(dic_eqls(dict1,dict2))

#ex4
def build_xml_element(tag, content, **kwargs):
    test = "<"+ tag
    for x in kwargs:
        test = test + " " +x + " =\\" + '"' + kwargs[x] + "\\" + '"'
    test = test+">" + content + "</"  +tag +">"
    return test


print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))

#ex5
def validate_dict(key, suffix, preffix, dictionary):
    for word, val in dictionary.items():
        hasSuffix = False
        hasPrefix = False
        for parser in range(0,len(word)):
            if word[0 : parser] == preffix:
                hasPrefix = True
                pos1 = parser
        for parser in range(0, len(word)):
            if word[len(word) - parser : len(word)] == suffix:  
                hasSuffix = True
                pos2 = len(word) - parser
        hasKey = False
        if (hasPrefix and hasSuffix):
            for parser1 in range(pos1, pos2 + 1):
                for parser2 in range(pos1, pos2 + 1):
                    if (word[parser1 : parser2] == key):
                        hasKey = True
        if not hasKey:
            return False
    return True

dictt = {'preakeyasuf': '1', 'prekeysuf': "2"}

print(validate_dict("key", "suf", "pre", dictt))

#ex6
def functie(lista):
    a = []
    a = list(set(lista))
    b= len(lista) - len(a)
    return a,b

print(functie([1,2,3,4,5,6,1,2,3,4,1,2,3,10,5]))

#ex7
def operatii (*args):
    dictionar = dict()
    for x in range(0,len(args)):
        for y in range(x+1,len(args)):
            union_string = str(args[x]) + " | " + str(args[y])+ ": "
            inter_string = str(args[x]) + " & " + str(args[y])+ ": "
            diff1_string = str(args[x]) + " - " + str(args[y])+ ": "
            diff2_string = str(args[y]) + " - " + str(args[x])+ ": "
            dictionar[union_string] = args[x].union(args[y])
            dictionar[inter_string] = args[x].intersection(args[y])
            dictionar[diff1_string] = args[x].difference(args[y])
            dictionar[diff2_string] = args[y].difference(args[x])
    return dictionar
x = {2,3,4,5}
y = {3,4,5}
z = {5}
dictionarul = operatii(x,y ,z)
for key,value in dictionarul.items():
    print(key, value)

#ex8
def loop(mapping):
    lista = []
    frecventa = []
    lista.append(mapping.get('start'))
    frecventa.append('start')
    start = mapping.get('start')
    while (True):
        if mapping.get(start) not in lista:
            lista.append(mapping.get(start))
            start = mapping.get(start)
        else:
            break

    return lista

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

#ex9
def my_function(*args, **kwargs):
    counter = 0
    for key,value in kwargs.items():
        if value in args:
            counter = counter + 1
    return counter

print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))