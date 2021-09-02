import os
import glob

directory = 'C:/Users/Максим/PycharmProjects/newdz22'
files = os.listdir(directory)
filter_path = os.path.join(directory, "*.txt")
filtered_files = glob.glob(filter_path)

def myfile():
    sizefiles = {}

    for lensize in filtered_files:
        with open(lensize, "r", encoding="UTF-8") as file:
            text = file.readlines()
            size = len(text)
            sizefiles[lensize] = size

    sorted_values = sorted(sizefiles.values())
    sorted_dict = {}
    for i in sorted_values:
        for k in sizefiles.keys():
            if sizefiles[k] == i:
                sorted_dict[k] = sizefiles[k]
                break

    print(sorted_dict)
    key = list(sorted_dict.keys())[0:3]

    print(type(key))

    for newfile in key:
        with open(newfile, "r", encoding="UTF-8") as file1:
            text1 = file1.readlines()
            with open("newfile.txt", "a", encoding="UTF-8") as file2:
                file2.write("".join(text1).strip())

myfile()
