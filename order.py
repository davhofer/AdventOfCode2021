import os
import re

days = 18
base_path = "./"


def make_dirs(n):
    for i in range(1,n+1):
        try:
            path = os.path.join(base_path,str(i))
            os.mkdir(path)
            print("Directory '% s' created" % str(i))
        except FileExistsError:
            print("Directory '% s' exists already" % str(i))
  

def move_files():
    base_path = "./"
    for file in filter(lambda x: "." in x, os.listdir()):
        try:
            matches = re.findall(r'\d+',file)
            if len(matches) > 0:
                subdir = matches[0] + "/"
                os.rename(base_path + file , base_path + subdir + file)
                print(f"Moved file {file} to subdirectory {subdir}")
        except:
            print(f"Error when moving file {file} to subdirectory {subdir}")




move_files()