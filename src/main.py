import os
import shutil
import sys
from generate_webpage import generate_pages_recursive

if len(sys.argv) <= 1:
    base_path = "/"
else:
    base_path = sys.argv[1]
public_path = os.path.join(".", "docs")
static_path = os.path.join(".", "static")

def main():
    generate_public_files()

def generate_public_files():
    if not os.path.exists(static_path):
        raise Exception(static_path + " does not exist")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.makedirs(public_path, exist_ok=True)
    copy_static_files(static_path, os.listdir(static_path))
    
def copy_static_files(path, files):
    if files == []:
        return
    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            relative_path = os.path.relpath(path, static_path)
            if relative_path == '.':
                dest_dir = public_path
            else:
                dest_dir = os.path.join(public_path, relative_path)
            os.makedirs(dest_dir, exist_ok=True)
            dest_file = os.path.join(dest_dir, file)
            print(f"Copying {file_path} to {dest_file}")
            shutil.copy(file_path, dest_file)
        else:
            new_dir = os.path.join(public_path, relative_path, file)
            os.makedirs(new_dir, exist_ok=True)
            
            copy_static_files(file_path, os.listdir(file_path))

    generate_pages_recursive("./content/", "./template.html", public_path, base_path)
    
    return

main()