import os
import os.path
import shutil

list_dir = []
for current_dir, dirs, files in os.walk("main"):
    print(current_dir, dirs, files)
    for file in files:
        if file[-3:] == ".py":
            if list_dir.count(current_dir) == 0:
                list_dir.append(current_dir)
print(list_dir)
list_dir.sort()
with open("task_2.4b.txt", "w") as file_write:
    for lis in list_dir:
        file_write.write(lis)
        file_write.write("\n")
