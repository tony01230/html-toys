# merge

from os import listdir
directory = "./test/"

files = []
for file in listdir(directory):
    if ".txt" in file and "dictionary" in file:
        files.append(file)

programs = []
for file in files:
    with open(directory+file, "r") as f:
        f = f.readlines()

    for program in f:
        programs.append(eval(program))

with open("output.txt", 'w') as f:
    f.writelines("\n".join(sorted([str(x) for x in programs])))