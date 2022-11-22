# ex1
import os

def print_ext(director):
    dir = os.listdir(director)
    lst = []
    for x in dir:
        lst.append(x.split(".")[-1])
    uniq_lst = list(set(lst))
    uniq_lst.sort()
    return uniq_lst
path = r'C:\Users\Cristian\OneDrive\Desktop\Pyhton L4'
print(print_ext(path))

# ex2
def func(director, fisier):
    file = open(fisier, 'w')
    dir = os.listdir(director)
    for x in dir:
        if x[0] == 'A' or x[0] == 'a':
            file.writelines(os.path.abspath(x)+'\n')

path_dir = r'C:\Users\Cristian\OneDrive\Desktop\Pyhton L4'
path_fis = r'C:\Users\Cristian\OneDrive\Desktop\Pyhton L4\test.txt'
func(path_dir,path_fis)

# ex4
def print_ext(director):
    dir = os.listdir(director)
    lst = []
    for x in dir:
        lst.append(x.split(".")[-1])
    uniq_lst = list(set(lst))
    uniq_lst.sort()
    return uniq_lst
path = input()
print(print_ext(path))

# ex5
def func(target, to_search):
    ok = 0
    lst = []
    if os.path.isfile(target):
        file = open(target,'r')
        file_str = str(file.read())
        file.close()
        if to_search in file_str:
            ok = 1
            lst.append(target)
            return lst
    elif os.path.isdir(target):
        for dirpath, dirs, files in os.walk(target):
            for filename in files:
                fname = os.path.join(dirpath,filename)
                if os.path.isfile(fname):
                    file = open(fname,'r', errors="ignore")
                    file_str = str(file.read())
                    file.close()
                    if to_search in file_str:
                        ok=1
                        lst.append(str(fname))
    else:
        raise ValueError

print(func(r'C:\Users\Cristian\OneDrive\Desktop\Pyhton L4\A.t', '123'))

# ex7
def check_access(file, mode):
    try:
        open(file, mode)
        return True
    except PermissionError:
        return False

def func(director):
    dictionary = {}
    dictionary['fullpath'] = director
    dictionary['file_size'] = os.path.getsize(director)
    if os.path.isfile(director):
        dictionary['file_extension'] = director.split(".")[-1]
    else:
        dictionary['file_extension'] = ""
    dictionary['can_read'] = check_access(director, 'r')
    dictionary['can_write'] = check_access(director, 'w')
    return dictionary

print(func(r'C:\Users\Cristian\OneDrive\Desktop\Pyhton L4'))

#ex8
def func(dir_path):
    lst = []
    dir = os.listdir(dir_path)
    for x in dir:
        lst.append(str(os.path.abspath(x)))
    return lst

print(func(r'C:\Users\Cristian\OneDrive'))