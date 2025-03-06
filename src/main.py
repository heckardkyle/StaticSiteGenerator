import os
import shutil
from textnode import TextType, TextNode

public_path = "./public/"
static_path = "./static/"

def main():
    generate_public_files()

def generate_public_files():
    if not os.path.exists(static_path):
        raise Exception("static/ does not exist")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    copy_static_files(static_path ,os.listdir(static_path))
    
def copy_static_files(path, files):
    if files == []:
        return
    for file in files:
        if os.path.isfile(path + file):
            shutil.copy(path + file, public_path + path[len(static_path):])
        else:
            new_dir = public_path + path[len(static_path):] + file + "/"
            os.mkdir(new_dir)
            copy_static_files(path + file + "/", os.listdir(path + file + "/"))
    
    return

main()