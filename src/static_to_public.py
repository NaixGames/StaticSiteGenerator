import os
import shutil

def static_to_public() -> None:
    copy_files_to_path_with_delete("./static", "./public")

def copy_files_to_path_with_delete(src_path: str, dst_path: str) -> None:
    abs_src_directory = os.path.abspath(src_path)
    dst_path = os.path.abspath(dst_path)
    
    print(f"This will copy everything in {abs_src_directory} to {dst_path}")

    if os.path.exists(dst_path):
        print(f"Cleaning existing {dst_path}")
        shutil.rmtree(dst_path)

    print(f"Creating folder {dst_path}")
    os.mkdir(dst_path)

    print(f"Starting copy process")
    copy_elements_in_path(src_path, dst_path)
    

def copy_elements_in_path(current_src_path: str, current_dst_path: str) -> None:
    elements = os.listdir(current_src_path)

    for element in elements:
        if os.path.isdir(current_src_path + "/" + element):
            print(f"Creating new folder element {element} contained in {current_src_path}")
            os.mkdir(current_dst_path + "/" + element)
            copy_elements_in_path(current_src_path + "/" + element, current_dst_path + "/" + element)
            continue

        if os.path.isfile(current_src_path + "/" + element):
            print(f"Copying file {element} contained in {current_src_path}")
            shutil.copy(current_src_path + "/" + element, current_dst_path)
            continue

        print(f"Element {element} is not file or folder. Idk what to do with this!")