import os
from pprint import pprint

# path = os.getcwd()
meta_files = []

def read_file(path_file):
    if os.path.exists(path_file):
        file = []
        meta_file = {}
        with open(path_file, "rt", encoding='utf-8') as f:
            file = f.readlines()
        f.close()
        return file
    else:
        return False

def meta(file,path):
    return (os.path.basename(path), len(file), "".join(file))

def write_file(name, count, text):
    with open("sorted/result.txt", "a", encoding='utf-8') as f:
        f.write(f'{name}\n')
        f.write(f'{count}\n')
        f.write(f'{text}\n')
    f.close()
    
file_1 = read_file("sorted/1.txt")
file_2 = read_file("sorted/2.txt")
file_3 = read_file("sorted/3.txt")
meta_files.append(meta(file_1,"sorted/1.txt")) if file_1 else print("Файл не существует")
meta_files.append(meta(file_2,"sorted/2.txt")) if file_2 else print("Файл не существует")
meta_files.append(meta(file_3,"sorted/3.txt")) if file_3 else print("Файл не существует")
meta_files.sort(key=lambda a: a[1])

for wr_file in meta_files:
    name, count, text = wr_file
    write_file(name, count, text.rstrip())