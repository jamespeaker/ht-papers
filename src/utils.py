import os

def ensure_dir_exists(path):
    directory_path = os.path.dirname(path)
    
    if directory_path and not os.path.exists(directory_path):
        os.makedirs(directory_path)